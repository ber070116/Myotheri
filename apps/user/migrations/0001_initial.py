# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-07 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('favorite_color', models.CharField(choices=[('white', 'Blanco'), ('silver', 'Plata'), ('gray', 'Gris'), ('black', 'Negro'), ('red', 'Rojo'), ('maroon', 'Granate'), ('yellow', 'Amarillo'), ('olive', 'Oliva'), ('lime', 'Lima'), ('green', 'Verde'), ('aqua', 'Agua'), ('teal', 'Trullo'), ('blue', 'Azul'), ('navy', 'Armada'), ('fuchsia', 'Fucsia'), ('purple', 'Purpura')], default='white', max_length=8)),
                ('musical_genres', models.CharField(choices=[('alternativo', 'Alternativo'), ('anime', 'Anime'), ('arabe', 'Arabe'), ('axe', 'Axé'), ('bachata', 'Bachata'), ('baladas', 'Baladas'), ('batucadas', 'Batucadas'), ('boleros', 'Boleros'), ('brasileras', 'Brasileras'), ('chaquenadas', 'Chaqueñadas'), ('chicha', 'Chicha'), ('clasica', 'Clasica'), ('country', 'Country'), ('criolla', 'Criolla'), ('cristiana', 'Cristiana'), ('cuarteto', 'Cuarteto'), ('cumbias', 'Cumbias'), ('dance', 'Dance'), ('disco', 'Disco'), ('dubstep', 'Dubstep'), ('electronica', 'Electronica'), ('emo', 'Emo'), ('eurodance', 'Eurodance'), ('flamenco', 'Flamenco'), ('gospel', 'Gospel'), ('gothic', 'Gothic'), ('gospel', 'Gospel'), ('hiphop', 'Hip Hop'), ('huyanos', 'Huyanos'), ('indu', 'Indu'), ('instrumentales', 'Instrumentales'), ('jazz', 'Jazz'), ('jpop', 'JPop'), ('jrock', 'JRock'), ('kizomba', 'Kizomba'), ('kpop', 'KPop'), ('krock', 'KRock'), ('lambadas', 'Lambadas'), ('llaneras', 'Llaneras'), ('los80', 'Los 80'), ('merengues', 'Merengues'), ('metal', 'Metal'), ('newwave', 'New Wave'), ('norteña', 'Norteña'), ('pop', 'Pop'), ('poprock', 'Pop Rock'), ('psicodelico', 'Psicodélico'), ('punk', 'Punk'), ('r&b', 'R&B'), ('rancheras', 'Rancheras'), ('rap', 'Rap'), ('reggae', 'Reggaeton'), ('mexicana', 'Mexicana'), ('rock', 'Rock'), ('romantica', 'Romantica'), ('salsa', 'Salsa'), ('samba', 'Samba'), ('sertanejo', 'Sertanejo'), ('soul', 'Soul'), ('soundtracks', 'Soundtracks'), ('takirai', 'Takirai'), ('tangos', 'Tangos'), ('techno', 'Techno'), ('texmex', 'Texmex'), ('trance', 'Trance'), ('trova', 'Trova'), ('vallenatos', 'Vallenatos')], default='alternativo', max_length=15)),
                ('favorite_number', models.IntegerField(null=True)),
                ('favorite_sport', models.CharField(choices=[('ala_delta', 'Ala delta'), ('acrobacia', 'Acrobacia'), ('acuatlon', 'Acuatlón'), ('aerobic', 'Aeróbic'), ('aikido', 'Aikido'), ('ajedrez', 'Ajedrez'), ('alpinismo', 'Alpinismo'), ('artesmar_ciales', 'Artes marciales'), ('atletismo', 'Atletismo'), ('automobilismo', 'Automobilismo'), ('baloncesto', 'Baloncesto'), ('balonmano', 'Balonmáno'), ('bailar', 'Billar'), ('billarda', 'Billarda'), ('birlos', 'Birlos'), ('bobsleigh', 'Bobsleigh'), ('bodyboard', 'Bodyboard'), ('boxeo', 'Boxeo'), ('badminton', 'Bádminton'), ('beisbol', 'Béisbol'), ('caza', 'Caza'), ('ciclismo', 'Ciclismo'), ('colombofilia', 'Colombofilia'), ('corfebol', 'Corfebol'), ('criquet', 'Críquet'), ('croquet', 'Cróquet'), ('cuadratlon', 'Cuadratlón'), ('curling', 'Curling'), ('danza', 'Danza'), ('deportiva', 'deportiva'), ('dardos', 'Dardos'), ('esgrima', 'Esgrima'), ('espeleoloxía', 'Espeleoloxía'), ('esquí', 'Esquí'), ('equitación', 'Equitación'), ('futbol', 'Fútbol'), ('futbol_playa', 'Fútbol playa'), ('futbol_sala', 'Fútbol sala'), ('golf', 'Golf'), ('gimnasia', 'Gimnasia'), ('gimnasia_ritmica', 'Gimnasia rítmica'), ('halterofilia', 'Halterofilia'), ('hipica', 'Hípica'), ('hockey_a_patines', 'Hóckey a patínes'), ('hockey_sobre_hierba', 'Hóckey sobre hierba'), ('hockey_sobre_hielo', 'Hóckey sobre hielo'), ('hockey', 'Hóckey'), ('hurling', 'Hurling'), ('judo', 'Judo'), ('karate', 'Karate'), ('kendo', 'Kendo'), ('kickboxing', 'Kickboxing'), ('kartin', 'Karting'), ('kung_fu', 'Kung Fu'), ('lacrosse', 'Lacrosse'), ('lucha', 'Lucha'), ('lucha_tradicional_gallega', 'Lucha tradicional gallega'), ('luciadas_extremas', 'Luciadas extremas'), ('sumerjo', 'Sumerjo'), ('motociclismo', 'Motociclismo'), ('motonautica', 'Motonáutica'), ('mhuai_thay', 'Mhuai Thay'), ('natacion', 'Natación'), ('octopush', 'Octopush'), ('orientación', 'Orientación'), ('paracaidismo', 'Paracaidismo'), ('parapente', 'Parapente'), ('parkour', 'Parkour'), ('patinaxe', 'Patinaxe'), ('paintball', 'Paintball'), ('pelota', 'Pelota'), ('pelota_valenciana', 'Pelota valenciana'), ('pelota_vasca', 'Pelota vasca'), ('pentatlon_moderno', 'Pentatlón moderno'), ('pesca_deportiva', 'Pesca deportiva'), ('petanca', 'Petanca'), ('piraguismo', 'Piragüismo'), ('polo', 'Polo'), ('remo', 'Remo'), ('rugby', 'Rugby'), ('salto_de_trampolin', 'Salto de trampolín'), ('sendeirismo', 'Sendeirismo'), ('softbol', 'Softbol'), ('shinty', 'Shinty'), ('skateboard', 'Skateboard'), ('skeleton', 'Skeleton'), ('snowboard', 'Snowboard'), ('speedball', 'Speedball'), ('squash', 'Squash'), ('sumo', 'Sumo'), ('superbikes', 'Superbikes'), ('surf', 'Surf'), ('tenis', 'Tenis'), ('tenis de mesa', 'Tenis de mesa'), ('tiro', 'Tiro'), ('tiro_con_arco', 'Tiro con arco'), ('triatlón', 'Triatlón'), ('taekwondo', 'Taekwondo'), ('Ultralixeiros', 'Ultralixeiros'), ('vela', 'Vela'), ('voleibol', 'Voleibol'), ('volei_playa', 'Volei playa'), ('valetudo', 'Valetudo'), ('waterpolo', 'Waterpolo'), ('windsurf', 'Windsurf'), ('wushu', 'Wushu'), ('win_tsun', 'Win Tsun'), ('xadrez', 'Xadrez'), ('ximnasia', 'Ximnasia'), ('ximnasia_rítmica', 'Ximnasia rítmica')], default='futbol', max_length=30)),
                ('hobby', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
