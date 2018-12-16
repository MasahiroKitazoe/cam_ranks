# Generated by Django 2.1.3 on 2018-12-16 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('pixel', models.IntegerField()),
                ('min_iso', models.IntegerField()),
                ('max_iso', models.IntegerField()),
                ('continuous_shooting_performance', models.FloatField()),
                ('shutter_speed', models.CharField(max_length=50)),
                ('monitor_size', models.FloatField()),
                ('monitor_pixel', models.FloatField()),
                ('shooting_num', models.IntegerField()),
                ('four_k', models.BooleanField()),
                ('wifi', models.BooleanField()),
                ('touch_panel', models.BooleanField()),
                ('move_panel', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('depth', models.FloatField()),
                ('f_value_wide', models.FloatField()),
                ('f_value_tele', models.FloatField()),
                ('shooting_num_with_finder', models.IntegerField()),
                ('bluetooth', models.CharField(max_length=20)),
                ('zoom', models.FloatField()),
                ('min_focus', models.IntegerField()),
                ('max_focus', models.IntegerField()),
                ('selfie', models.BooleanField()),
                ('waterploof', models.CharField(max_length=50)),
                ('gps', models.BooleanField()),
                ('nearest_shot', models.FloatField()),
                ('anti_shake', models.CharField(max_length=50)),
                ('five_axis_anti_shake', models.BooleanField()),
                ('nearest_shot_with_macro_mode', models.FloatField()),
                ('super_wide', models.BooleanField()),
                ('open_year', models.IntegerField()),
                ('open_month', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CameraType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Finder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finder_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camera.Camera')),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='camera_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camera.CameraType'),
        ),
        migrations.AddField(
            model_name='camera',
            name='finder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camera.Finder'),
        ),
        migrations.AddField(
            model_name='camera',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camera.Frame'),
        ),
        migrations.AddField(
            model_name='camera',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='camera.Maker'),
        ),
    ]
