# Documentação da AP2

Projeto: **E-commerce API (Django REST + AWS)** — evolução da AP1 para a nuvem.

Este documento descreve as etapas realizadas, as principais decisões técnicas e
as dificuldades enfrentadas com suas soluções.

---

## 1. Etapas realizadas

1. **Reaproveitamento da base da AP1** — parti do projeto Django REST já
   existente, com as entidades `Produto` e `Categoria` (FK de Produto para
   Categoria), mantendo serializers, views (ViewSets) e rotas.

2. **Configuração condicional do banco** — o `settings.py` foi ajustado para
   usar **MySQL no AWS RDS** quando as variáveis de ambiente `RDS_*` estiverem
   presentes, e cair em **SQLite** automaticamente no ambiente local. Isso
   permite desenvolver localmente sem nenhuma infraestrutura AWS.

3. **Armazenamento de mídia no S3** — Quando `AWS_STORAGE_BUCKET_NAME` está definido, as imagens dos
   produtos são enviadas e servidas a partir do bucket S3.

4. **Uso de variáveis de ambiente** — todos os dados sensíveis (chave secreta,
   credenciais do banco, nome do bucket e região) foram retirados do código e
   passam a ser lidos do ambiente, configurados nas *Environment properties* do
   Elastic Beanstalk.

5. **Deploy e validação na AWS** — criação do RDS, do bucket S3 e do ambiente
   EB; subida do pacote `app.zip`; criação do superusuário; e teste dos
   endpoints da API e do Django Admin no ambiente em produção.

---

## 2. Principais decisões técnicas

- **Configuração por ambiente, não por arquivo separado.** Em vez de manter um
  `settings_prod.py`, optamos por um único `settings.py` que detecta as
  variáveis de ambiente. Menos arquivos para manter e o mesmo código roda local
  e na nuvem.

- **MySQL gerenciado (RDS) em vez de instalar o banco na EC2.** Reduz o esforço
  de operação (backup, atualização, disponibilidade ficam com a AWS) e isola o
  banco da instância de aplicação.

- **Mídia no S3 com `django-storages`.** Mantém a aplicação *stateless*: como o
  Elastic Beanstalk pode recriar/substituir instâncias EC2, guardar imagens no
  disco local seria perdê-las. O S3 garante durabilidade e URLs estáveis.


---

## 3. Dificuldades e soluções

- **Conexão recusada com o RDS.** No primeiro deploy o `migrate` falhava por
  *connection timeout*. Causa: o Security Group do RDS não permitia tráfego da
  aplicação. **Solução:** liberar a porta 3306 para o Security Group do
  ambiente Elastic Beanstalk. O hook de predeploy foi escrito para não derrubar
  o deploy caso o `migrate` falhe, facilitando o diagnóstico.

- **Imagens não apareciam após o deploy.** As imagens enviadas sumiam quando a
  instância era reiniciada, porque estavam no disco local. **Solução:**
  configurar o S3 como `DEFAULT_FILE_STORAGE` e ajustar o `MEDIA_URL` para
  apontar para o bucket.

- **Acesso às imagens no S3 negado.** As URLs retornavam erro de acesso.
  **Solução:** habilitar leitura pública dos objetos (`AWS_DEFAULT_ACL =
  'public-read'`) e configurar as permissões/política do bucket.

- **Segredos no código.** A `SECRET_KEY` e credenciais estavam embutidas.
  **Solução:** mover tudo para variáveis de ambiente, com *fallbacks* apenas
  para o ambiente local de desenvolvimento.


---

## 4. Resultado

A aplicação roda no Elastic Beanstalk com o banco no RDS MySQL e as imagens dos
produtos no S3, controlada por variáveis de ambiente. Os endpoints REST de
`produtos` e `categorias` respondem em produção e o Django Admin está
acessível com o usuário administrador.
