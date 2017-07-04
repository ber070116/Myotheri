from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# import para los tokens
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UsuarioManager(BaseUserManager):
    def crear_usuario(
        self,
        nombre_usuario,
        email,
        fecha_nacimiento,
        clave=None
    ):
        if not email and not nombre_usuario:
            raise ValueError('Users must have an email address')

        usuario = self.model(
            nombre_usuario=nombre_usuario,
            email=self.normalize_email(email),
            fecha_nacimiento=fecha_nacimiento,
        )

        usuario.set_password(clave)
        usuario.save(using=self._db)
        return usuario

    # funci
    def crear_superusuario(
        self,
        nombre_usuario,
        email,
        fecha_nacimiento,
        clave
    ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        usuario = self.crear_usuario(
            nombre_usuario,
            email,
            clave=clave,
            fecha_nacimiento=fecha_nacimiento,
        )
        usuario.administrador = True
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    # colores para el select
    COLORES = (
        ('white', 'Blanco'),
        ('silver', 'Plata'),
        ('gray', 'Gris'),
        ('black', 'Negro'),
        ('red', 'Rojo'),
        ('maroon', 'Granate'),
        ('yellow', 'Amarillo'),
        ('olive', 'Oliva'),
        ('lime', 'Lima'),
        ('green', 'Verde'),
        ('aqua', 'Agua'),
        ('teal', 'Trullo'),
        ('blue', 'Azul'),
        ('navy', 'Armada'),
        ('fuchsia', 'Fucsia'),
        ('purple', 'Purpura')
    )

    GENEROS_MUSICALES = (
        ('alternativo', 'Alternativo'),
        ('anime', 'Anime'),
        ('arabe', 'Arabe'),
        ('axe', 'Axé'),
        ('bachata', 'Bachata'),
        ('baladas', 'Baladas'),
        ('batucadas', 'Batucadas'),
        ('boleros', 'Boleros'),
        ('brasileras', 'Brasileras'),
        ('chaquenadas', 'Chaqueñadas'),
        ('chicha', 'Chicha'),
        ('clasica', 'Clasica'),
        ('country', 'Country'),
        ('criolla', 'Criolla'),
        ('cristiana', 'Cristiana'),
        ('cuarteto', 'Cuarteto'),
        ('cumbias', 'Cumbias'),
        ('dance', 'Dance'),
        ('disco', 'Disco'),
        ('dubstep', 'Dubstep'),
        ('electronica', 'Electronica'),
        ('emo', 'Emo'),
        ('eurodance', 'Eurodance'),
        ('flamenco', 'Flamenco'),
        ('gospel', 'Gospel'),
        ('gothic', 'Gothic'),
        ('gospel', 'Gospel'),
        ('hiphop', 'Hip Hop'),
        ('huyanos', 'Huyanos'),
        ('indu', 'Indu'),
        ('instrumentales', 'Instrumentales'),
        ('jazz', 'Jazz'),
        ('jpop', 'JPop'),
        ('jrock', 'JRock'),
        ('kizomba', 'Kizomba'),
        ('kpop', 'KPop'),
        ('krock', 'KRock'),
        ('lambadas', 'Lambadas'),
        ('llaneras', 'Llaneras'),
        ('los80', 'Los 80'),
        ('merengues', 'Merengues'),
        ('metal', 'Metal'),
        ('newwave', 'New Wave'),
        ('norteña', 'Norteña'),
        ('pop', 'Pop'),
        ('poprock', 'Pop Rock'),
        ('psicodelico', 'Psicodélico'),
        ('punk', 'Punk'),
        ('r&b', 'R&B'),
        ('rancheras', 'Rancheras'),
        ('rap', 'Rap'),
        ('reggae', 'Reggaeton'),
        ('mexicana', 'Mexicana'),
        ('rock', 'Rock'),
        ('romantica', 'Romantica'),
        ('salsa', 'Salsa'),
        ('samba', 'Samba'),
        ('sertanejo', 'Sertanejo'),
        ('soul', 'Soul'),
        ('soundtracks', 'Soundtracks'),
        ('takirai', 'Takirai'),
        ('tangos', 'Tangos'),
        ('techno', 'Techno'),
        ('texmex', 'Texmex'),
        ('trance', 'Trance'),
        ('trova', 'Trova'),
        ('vallenatos', 'Vallenatos'),
    )

    DEPORTES = (
        ('ala_delta', 'Ala delta'),
        ('acrobacia', 'Acrobacia'),
        ('acuatlon', 'Acuatlón'),
        ('aerobic', 'Aeróbic'),
        ('aikido', 'Aikido'),
        ('ajedrez', 'Ajedrez'),
        ('alpinismo', 'Alpinismo'),
        ('artesmar_ciales', 'Artes marciales'),
        ('atletismo', 'Atletismo'),
        ('automobilismo', 'Automobilismo'),
        ('baloncesto', 'Baloncesto'),
        ('balonmano', 'Balonmáno'),
        ('bailar', 'Billar'),
        ('billarda', 'Billarda'),
        ('birlos', 'Birlos'),
        ('bobsleigh', 'Bobsleigh'),
        ('bodyboard', 'Bodyboard'),
        ('boxeo', 'Boxeo'),
        ('badminton', 'Bádminton'),
        ('beisbol', 'Béisbol'),
        ('caza', 'Caza'),
        ('ciclismo', 'Ciclismo'),
        ('colombofilia', 'Colombofilia'),
        ('corfebol', 'Corfebol'),
        ('criquet', 'Críquet'),
        ('croquet', 'Cróquet'),
        ('cuadratlon', 'Cuadratlón'),
        ('curling', 'Curling'),
        ('danza', 'Danza'),
        ('deportiva', 'deportiva'),
        ('dardos', 'Dardos'),
        ('esgrima', 'Esgrima'),
        ('espeleoloxía', 'Espeleoloxía'),
        ('esquí', 'Esquí'),
        ('equitación', 'Equitación'),
        ('futbol', 'Fútbol'),
        ('futbol_playa', 'Fútbol playa'),
        ('futbol_sala', 'Fútbol sala'),
        ('golf', 'Golf'),
        ('gimnasia', 'Gimnasia'),
        ('gimnasia_ritmica', 'Gimnasia rítmica'),
        ('halterofilia', 'Halterofilia'),
        ('hipica', 'Hípica'),
        ('hockey_a_patines', 'Hóckey a patínes'),
        ('hockey_sobre_hierba', 'Hóckey sobre hierba'),
        ('hockey_sobre_hielo', 'Hóckey sobre hielo'),
        ('hockey', 'Hóckey'),
        ('hurling', 'Hurling'),
        ('judo', 'Judo'),
        ('karate', 'Karate'),
        ('kendo', 'Kendo'),
        ('kickboxing', 'Kickboxing'),
        ('kartin', 'Karting'),
        ('kung_fu', 'Kung Fu'),
        ('lacrosse', 'Lacrosse'),
        ('lucha', 'Lucha'),
        ('lucha_tradicional_gallega', 'Lucha tradicional gallega'),
        ('luciadas_extremas', 'Luciadas extremas'),
        ('sumerjo', 'Sumerjo'),
        ('motociclismo', 'Motociclismo'),
        ('motonautica', 'Motonáutica'),
        ('mhuai_thay', 'Mhuai Thay'),
        ('natacion', 'Natación'),
        ('octopush', 'Octopush'),
        ('orientación', 'Orientación'),
        ('paracaidismo', 'Paracaidismo'),
        ('parapente', 'Parapente'),
        ('parkour', 'Parkour'),
        ('patinaxe', 'Patinaxe'),
        ('paintball', 'Paintball'),
        ('pelota', 'Pelota'),
        ('pelota_valenciana', 'Pelota valenciana'),
        ('pelota_vasca', 'Pelota vasca'),
        ('pentatlon_moderno', 'Pentatlón moderno'),
        ('pesca_deportiva', 'Pesca deportiva'),
        ('petanca', 'Petanca'),
        ('piraguismo', 'Piragüismo'),
        ('polo', 'Polo'),
        ('remo', 'Remo'),
        ('rugby', 'Rugby'),
        ('salto_de_trampolin', 'Salto de trampolín'),
        ('sendeirismo', 'Sendeirismo'),
        ('softbol', 'Softbol'),
        ('shinty', 'Shinty'),
        ('skateboard', 'Skateboard'),
        ('skeleton', 'Skeleton'),
        ('snowboard', 'Snowboard'),
        ('speedball', 'Speedball'),
        ('squash', 'Squash'),
        ('sumo', 'Sumo'),
        ('superbikes', 'Superbikes'),
        ('surf', 'Surf'),
        ('tenis', 'Tenis'),
        ('tenis de mesa', 'Tenis de mesa'),
        ('tiro', 'Tiro'),
        ('tiro_con_arco', 'Tiro con arco'),
        ('triatlón', 'Triatlón'),
        ('taekwondo', 'Taekwondo'),
        ('Ultralixeiros', 'Ultralixeiros'),
        ('vela', 'Vela'),
        ('voleibol', 'Voleibol'),
        ('volei_playa', 'Volei playa'),
        ('valetudo', 'Valetudo'),
        ('waterpolo', 'Waterpolo'),
        ('windsurf', 'Windsurf'),
        ('wushu', 'Wushu'),
        ('win_tsun', 'Win Tsun'),
        ('xadrez', 'Xadrez'),
        ('ximnasia', 'Ximnasia'),
        ('ximnasia_rítmica', 'Ximnasia rítmica')
    )

    nombre_usuario = models.CharField(max_length=25, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
    administrador = models.BooleanField(default=False)

    # gustos
    # COLOR
    color_favorito = models.CharField(
        max_length=8,
        choices=COLORES,
        default='white'
    )

    # GENERO
    genero_musical = models.CharField(
        max_length=15,
        choices=GENEROS_MUSICALES,
        default='alternativo'
    )
    numero_favorito = models.IntegerField(null=True)

    # DEPORTE
    deporte_favorito = models.CharField(
        max_length=30,
        choices=DEPORTES,
        default='futbol'
    )
    hobby = models.CharField(max_length=25)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['email', 'fecha_nacimiento']

    def get_nombre_usuario(self):

        return self.nombre_usuario

    def get_email(self):

        return self.email

    def __str__(self):
        return self.nombre_usuario

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.administrador


# token para los usuarios
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
