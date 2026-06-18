<<<<<<< HEAD
# E-commerce API — AP2 (Django REST + AWS)

API REST construída com **Django REST Framework**, evoluída a partir da AP1 e
preparada para rodar na nuvem com **AWS RDS (MySQL)**, **S3** e
**Elastic Beanstalk** (deploy).

---

## Arquitetura da solução (AP1 → AP2)

Na **AP1** o projeto era uma API Django REST simples, com a entidade `Produto`
e a classe `Categoria`.

Na **AP2** a mesma base evoluiu para um ambiente de nuvem, sem mudar a regra de
negócio das entidades:

```
Internet
   │
   ▼
[Elastic Beanstalk]  ←── app.zip (código Django)
   │  
   │               │
   ▼               ▼
[RDS MySQL]     [S3 Bucket]
 banco de dados  imagens dos produtos
```


---

## Execução local

Pré-requisitos: Python 3.12 e pip.

```bash
# 1. Ambiente virtual
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Dependências
pip install -r requirements.txt

# 3. Banco local (SQLite) e migrações
python manage.py migrate

# 4. Usuário administrador
python manage.py createsuperuser

# 5. Rodar
python manage.py runserver
```


## Variáveis de ambiente

Nenhum dado sensível fica no código. As variáveis abaixo são lidas pelo
`settings.py` (no EB elas são configuradas em *Configuration → Environment
properties*):

| Variável                  | Uso                                  |
|---------------------------|--------------------------------------|
| `DJANGO_SECRET_KEY`       | Chave secreta do Django              |
| `DJANGO_DEBUG`            | `True`/`False`                       |
| `RDS_HOSTNAME`            | Endpoint do RDS MySQL                |
| `RDS_DB_NAME`             | Nome do banco                        |
| `RDS_USERNAME`            | Usuário do banco                     |
| `RDS_PASSWORD`            | Senha do banco                       |
| `RDS_PORT`                | Porta (default `3306`)               |
| `AWS_STORAGE_BUCKET_NAME` | Nome do bucket S3                    |
| `AWS_S3_REGION_NAME`      | Região do bucket


---

## Deploy na AWS (resumo)


1. **Gerar o pacote**: compactar o conteúdo do projeto em `app.zip`.
2. **S3**: criar o bucket e habilitar acesso público de leitura para a mídia.
3. **Elastic Beanstalk**: criar um ambiente Python, subir o `app.zip` e
   preencher as *Environment properties* (variáveis acima).

---

---

## Link da API em produção

http://api-produtos-caio-env.eba-v3eym6ck.us-east-1.elasticbeanstalk.com/

---


```
=======
# Big-data-e-Cloud-Computing---AP2
>>>>>>> e116a11585dac9c8234013b5bf0c85801294137f
