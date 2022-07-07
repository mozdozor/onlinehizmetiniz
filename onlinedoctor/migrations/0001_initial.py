# Generated by Django 3.2.6 on 2022-07-07 19:07

import autoslug.fields
import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_doctor', models.BooleanField(default=False)),
                ('doctor_okey', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
                ('define_profession', models.CharField(default='', max_length=450)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='get_full_name', unique=True)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Kadın'), ('male', 'Erkek')], default='None', max_length=10, null=True, verbose_name='Cinsiyetiniz')),
                ('blood_group', models.CharField(blank=True, choices=[('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('0-', '0-'), ('0+', '0+')], default='None', max_length=10, null=True, verbose_name='Kan Grubunuz')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('phone_number', models.CharField(max_length=250)),
                ('unvan', models.CharField(default='', max_length=250)),
                ('image', models.ImageField(blank=True, default='avatar/no-avatar.png', null=True, upload_to='doctor_images')),
                ('file', models.FileField(blank=True, null=True, upload_to='doctors_file')),
                ('kimlik', models.FileField(blank=True, null=True, upload_to='doctors_file')),
                ('about', models.TextField(blank=True, default='', null=True)),
                ('clinic_name', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('clinic_address', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('clinic_image', models.ImageField(blank=True, null=True, upload_to='doctor_images/clinic_images')),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('cityCode', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('country', models.CharField(blank=True, default='Türkiye', max_length=50, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=450, null=True)),
                ('is_free', models.BooleanField(default=True)),
                ('custom_price', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('average_star', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('none_average_star', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('parent_comments_count', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('appointment_minute', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('services', models.CharField(blank=True, default='', max_length=750, null=True)),
                ('specializations', models.CharField(blank=True, default='', max_length=750, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active_day', models.CharField(blank=True, default='Pazartesi', max_length=50, null=True)),
                ('online', models.CharField(blank=True, default='offline', max_length=10, null=True)),
                ('is_active_now', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'verbose_name_plural': 'Kullanıcılar',
                'db_table': 'customUser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='alanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='alan_images')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Alan',
                'verbose_name_plural': 'Alanlar',
                'db_table': 'alan',
            },
        ),
        migrations.CreateModel(
            name='alanYazilarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_title', models.CharField(max_length=250)),
                ('bottom_title', models.TextField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Alan Yazı',
                'verbose_name_plural': 'Alan Yazıları',
                'db_table': 'alanYazi',
            },
        ),
        migrations.CreateModel(
            name='bannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_title', models.CharField(max_length=250)),
                ('bottom_title', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='doctorFeatureIndexModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='doktor_ozellik_image')),
                ('yazi', ckeditor.fields.RichTextField()),
                ('top_title', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'doctorFeatureIndex_Ayari',
                'verbose_name_plural': 'doctorFeatureIndex_Ayari',
                'db_table': 'doctorFeatureIndex',
            },
        ),
        migrations.CreateModel(
            name='featureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='doktor_ozellik_image/feature')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'feature_model',
                'verbose_name_plural': 'feature_model',
                'db_table': 'feature',
            },
        ),
        migrations.CreateModel(
            name='footerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aciklamaYazisi', ckeditor.fields.RichTextField()),
                ('facebook', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram', models.CharField(blank=True, max_length=250, null=True)),
                ('pinterest', models.CharField(blank=True, max_length=250, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Footer_Ayari',
                'verbose_name_plural': 'Footer_Ayari',
                'db_table': 'footer',
            },
        ),
        migrations.CreateModel(
            name='IletisimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whoIs', models.CharField(choices=[('nobody', 'Lütfen kim olduğunuzu belirtiniz'), ('Ben bir doktorum ve sitenize üyeyim', 'Ben bir doktorum ve sitenize üyeyim'), ('Ben bir doktorum ancak sitenize üye değilim', 'Ben bir doktorum ancak sitenize üye değilim'), ('Hastayım/Ziyaretçiyim', 'Hastayım/Ziyaretçiyim'), ('Medya ve İşbirliği', 'Medya ve İşbirliği')], default='None', max_length=150)),
                ('fullName', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('subject', models.CharField(max_length=100)),
                ('mesaj', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('okundu_bilgisi', models.CharField(default='okunmadı', max_length=30)),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişim',
                'db_table': 'iletisim',
            },
        ),
        migrations.CreateModel(
            name='indexDoktorlarYaziModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazi', ckeditor.fields.RichTextField()),
                ('top_title', models.CharField(blank=True, max_length=250, null=True)),
                ('bottom_title', models.TextField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'İndex Yazısı',
                'verbose_name_plural': 'İndex Yazısı',
                'db_table': 'İndex_Yazisi',
            },
        ),
        migrations.CreateModel(
            name='logoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anaLogo', models.ImageField(blank=True, null=True, upload_to='logolar')),
                ('footerLogo', models.ImageField(blank=True, null=True, upload_to='logolar')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logolar',
                'db_table': 'logolar',
            },
        ),
        migrations.CreateModel(
            name='TimeScheduleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(blank=True, choices=[(0, '-'), (15, '15 dk'), (30, '30 dk'), (45, '45 dk'), (60, '60 dk')], default='None', null=True)),
                ('day', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('money', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('starting_time', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('finishing_time', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('date', models.DateField(null=True)),
                ('is_paid', models.CharField(default='no', max_length=50)),
                ('meeting_method', models.CharField(blank=True, default='ourSystem', max_length=50, null=True)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeschedules', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'müsait zaman',
                'verbose_name_plural': 'müsait zamanlar',
                'db_table': 'timeschedule',
            },
        ),
        migrations.CreateModel(
            name='socialMediaDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter', models.CharField(blank=True, max_length=250, null=True)),
                ('instagram', models.CharField(blank=True, max_length=250, null=True)),
                ('pinterest', models.CharField(blank=True, max_length=250, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_media', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sosyal Medya',
                'verbose_name_plural': 'Sosyal Medya Hesapları',
                'db_table': 'socialMediaDoctor',
            },
        ),
        migrations.CreateModel(
            name='iletisimSettingsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp', models.CharField(blank=True, max_length=250, null=True)),
                ('zoom', models.CharField(blank=True, max_length=250, null=True)),
                ('skype', models.CharField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iletisimSettings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'iletisim_ayarlar_',
                'verbose_name_plural': 'iletisim_ayarlari_',
                'db_table': 'iletisimSettingsModel',
            },
        ),
        migrations.CreateModel(
            name='FavouriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients_favourite', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favori',
                'verbose_name_plural': 'Favoriler',
                'db_table': 'favourites',
            },
        ),
        migrations.CreateModel(
            name='experienceDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(blank=True, max_length=250, null=True)),
                ('time', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencesofdoctor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tecrübe',
                'verbose_name_plural': 'Tecrübeler',
                'db_table': 'experienceDoctor',
            },
        ),
        migrations.CreateModel(
            name='educationDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=250, null=True)),
                ('college', models.CharField(blank=True, max_length=250, null=True)),
                ('year_of_completion', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educationsofdoctor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Eğitim',
                'verbose_name_plural': 'Eğitimler',
                'db_table': 'degreeDoctor',
            },
        ),
        migrations.CreateModel(
            name='deletedAppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField()),
                ('day', models.CharField(max_length=250)),
                ('money', models.PositiveSmallIntegerField()),
                ('starting_time', models.CharField(max_length=250)),
                ('finishing_time', models.CharField(max_length=250)),
                ('meeting_method', models.CharField(blank=True, default='ourSystem', max_length=50, null=True)),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deletedAppointmentsOfDoctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deleetdAppointmentsOfPatient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'silinenFatura',
                'verbose_name_plural': 'silinenFaturalar',
                'db_table': 'deletedAppointments',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_recommend', models.BooleanField(default=False)),
                ('star', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('none_star', models.PositiveSmallIntegerField(blank=True, default=5, null=True)),
                ('comment', models.TextField(blank=True, default='', null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='his_comments', to=settings.AUTH_USER_MODEL)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_comments', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='onlinedoctor.commentmodel')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'db_table': 'comment',
                'ordering': ('-created_date',),
            },
        ),
        migrations.CreateModel(
            name='ClinicImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_image', models.ImageField(blank=True, null=True, upload_to='doctor_images/clinic_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clinicimages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='awardsDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(blank=True, max_length=250, null=True)),
                ('year', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='awardsofdoctor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ödül',
                'verbose_name_plural': 'Ödüller',
                'db_table': 'awardsDoctor',
            },
        ),
        migrations.CreateModel(
            name='appointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField()),
                ('day', models.CharField(max_length=250)),
                ('money', models.PositiveSmallIntegerField()),
                ('starting_time', models.CharField(max_length=250)),
                ('finishing_time', models.CharField(max_length=250)),
                ('meeting_method', models.CharField(blank=True, default='ourSystem', max_length=50, null=True)),
                ('date', models.DateField()),
                ('totalDuration', models.TimeField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointmentsOfDoctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointmentsOfPatient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'fatura',
                'verbose_name_plural': 'faturalar',
                'db_table': 'appointments',
            },
        ),
    ]
