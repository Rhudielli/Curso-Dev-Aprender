# Herança

# class Pai
class Camera: # tambem é valido > Camera() / Camera(object)
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels')

# class Filho > Herança class Pai
class cameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_cameras = quantidade_cameras

    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    def tirar_foto(self, camera_utilizar):
        print(f'Foto tirada com a camera {self.marca} com a qualidade de {self.megapixels} megapixels, utilizando camera #{camera_utilizar}')

# class Filho > Herança class Pai
class CameraSeguranca(Camera):
    def __init__(self, marca, megapixels, horas_maxima_gravacao):
        super().__init__(marca, megapixels)
        self.horas_maxima_gravacao = horas_maxima_gravacao

    def rotacionar_camera(self, direcao):
        print(f'Rotacionando a camera para {direcao}')

print(issubclass(cameraCelular, Camera))
print(issubclass(CameraSeguranca, Camera))