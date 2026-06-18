from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer


@api_view(['GET'])
def health_check(request):
    """Endpoint de saúde — usado pelo EB para verificar se a app está no ar."""
    return Response({'status': 'ok', 'mensagem': 'API funcionando!'})


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de Categorias.

    - GET    /api/categorias/        → lista todas
    - POST   /api/categorias/        → cria nova
    - GET    /api/categorias/{id}/   → detalhe
    - PUT    /api/categorias/{id}/   → atualiza
    - DELETE /api/categorias/{id}/   → remove
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de Produtos.

    - GET    /api/produtos/        → lista todos
    - POST   /api/produtos/        → cria novo
    - GET    /api/produtos/{id}/   → detalhe
    - PUT    /api/produtos/{id}/   → atualiza
    - DELETE /api/produtos/{id}/   → remove
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
