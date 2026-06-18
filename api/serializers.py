from rest_framework import serializers
from .models import Produto, Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ('criado_em', 'atualizado_em')


class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Produto
        fields = '__all__'
        read_only_fields = ('criado_em', 'atualizado_em')
