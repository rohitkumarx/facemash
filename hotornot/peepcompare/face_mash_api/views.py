from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView

	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
)

from peepcompare.models import FaceMash
from .pagination import (
	PostLimitOffsetPagination,
	PostPageNumberPagination
)

from .serializers import (
FacemashListSerializer, 
FacemashDetailSerializer,
FacemashCreateUpdateSerializer
)

from .permissions import IsOwnerOrReadOnly

from rest_framework.filters import (

	SearchFilter,
	OrderingFilter,

)

from rest_framework.pagination import (
	PageNumberPagination,
	LimitOffsetPagination

)


class FaceMashListApiView(ListAPIView):
	queryset = FaceMash.objects.all()
	serializer_class = FacemashListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name']
	pagination_class = PostPageNumberPagination #PostLimitOffsetPagination #PageNumberPagination

class FaceMashUpdateApiView(RetrieveUpdateAPIView):
	queryset = FaceMash.objects.all()
	serializer_class = FacemashCreateUpdateSerializer
	permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(user = self.request.user)

class FaceMashDeleteApiView(DestroyAPIView):
	queryset = FaceMash.objects.all()
	serializer_class = FacemashListSerializer

class FMDetailApiView(RetrieveAPIView):
	queryset = FaceMash.objects.all()
	serializer_class = FacemashDetailSerializer

class FaceMashCreateApiView(CreateAPIView):
	queryset = FaceMash.objects.all()
	serializer_class = FacemashCreateUpdateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user = self.request.user, name = 'Generic name')
