# Generated by Django 2.1.3 on 2019-01-14 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('min_price', models.IntegerField(null=True, verbose_name='price')),
                ('max_price', models.IntegerField(null=True, verbose_name='price')),
                ('min_pixel', models.IntegerField(null=True, verbose_name='pixel')),
                ('max_pixel', models.IntegerField(null=True, verbose_name='pixel')),
                ('min_iso', models.IntegerField(null=True, verbose_name='iso')),
                ('max_iso', models.IntegerField(null=True, verbose_name='iso')),
                ('min_continuous_shooting_performance', models.FloatField(null=True, verbose_name='continuous_shooting_performance')),
                ('max_continuous_shooting_performance', models.FloatField(null=True, verbose_name='continuous_shooting_performance')),
                ('min_shutter_speed', models.CharField(max_length=50, null=True, verbose_name='shutter_speed')),
                ('max_shutter_speed', models.CharField(max_length=50, null=True, verbose_name='shutter_speed')),
                ('min_monitor_size', models.FloatField(null=True, verbose_name='monitor_size')),
                ('max_monitor_size', models.FloatField(null=True, verbose_name='monitor_size')),
                ('min_monitor_pixel', models.FloatField(null=True, verbose_name='monitor_pixel')),
                ('max_monitor_pixel', models.FloatField(null=True, verbose_name='monitor_pixel')),
                ('min_shooting_num', models.IntegerField(null=True, verbose_name='num_of_shooting')),
                ('max_shooting_num', models.IntegerField(null=True, verbose_name='num_of_shooting')),
                ('four_k', models.BooleanField(null=True, verbose_name='four_k')),
                ('wifi', models.BooleanField(null=True, verbose_name='wifi')),
                ('touch_panel', models.BooleanField(null=True, verbose_name='touch_panel')),
                ('move_panel', models.BooleanField(null=True, verbose_name='move_panel')),
                ('min_weight', models.FloatField(null=True, verbose_name='weight')),
                ('max_weight', models.FloatField(null=True, verbose_name='weight')),
                ('min_width', models.FloatField(null=True, verbose_name='width')),
                ('max_width', models.FloatField(null=True, verbose_name='width')),
                ('min_height', models.FloatField(null=True, verbose_name='height')),
                ('max_height', models.FloatField(null=True, verbose_name='height')),
                ('min_depth', models.FloatField(null=True, verbose_name='depth')),
                ('max_depth', models.FloatField(null=True, verbose_name='depth')),
                ('frame_id', models.IntegerField(null=True, verbose_name='frame_id')),
                ('maker_id', models.IntegerField(null=True, verbose_name='maker_id')),
                ('finder_id', models.IntegerField(null=True, verbose_name='finder_id')),
                ('min_f_value_tele', models.FloatField(null=True, verbose_name='f_value')),
                ('max_f_value_tele', models.FloatField(null=True, verbose_name='f_value')),
                ('min_shooting_num_with_finder', models.IntegerField(null=True, verbose_name='num_of_shooting_with_finder')),
                ('max_shooting_num_with_finder', models.IntegerField(null=True, verbose_name='num_of_shooting_with_finder')),
                ('bluetooth', models.BooleanField(null=True, verbose_name='bluetooth')),
                ('min_zoom', models.FloatField(null=True, verbose_name='zoom')),
                ('max_zoom', models.FloatField(null=True, verbose_name='zoom')),
                ('min_focus', models.IntegerField(null=True, verbose_name='min_focus')),
                ('max_focus', models.IntegerField(null=True, verbose_name='max_focus')),
                ('selfie', models.BooleanField(null=True, verbose_name='selfie')),
                ('waterploof', models.BooleanField(null=True, verbose_name='waterploof')),
                ('min_water_depth', models.IntegerField(null=True, verbose_name='water_depth')),
                ('max_water_depth', models.IntegerField(null=True, verbose_name='water_depth')),
                ('gps', models.BooleanField(null=True, verbose_name='gps')),
                ('min_nearest_shot', models.FloatField(null=True, verbose_name='nearest_shot')),
                ('max_nearest_shot', models.FloatField(null=True, verbose_name='nearest_shot')),
                ('anti_shake', models.BooleanField(null=True, verbose_name='anti_shake')),
                ('five_axis_anti_shake', models.BooleanField(null=True, verbose_name='five_axis_anti_shake')),
                ('min_nearest_shot_with_macro_mode', models.FloatField(null=True, verbose_name='nearest_shot_with_macro_mode')),
                ('max_nearest_shot_with_macro_mode', models.FloatField(null=True, verbose_name='nearest_shot_with_macro_mode')),
                ('min_f_value_wide', models.FloatField(null=True, verbose_name='f_value_wide')),
                ('max_f_value_wide', models.FloatField(null=True, verbose_name='f_value_wide')),
                ('super_wide', models.BooleanField(null=True, verbose_name='super_wide')),
                ('min_open_date', models.DateField(null=True, verbose_name='min_open_date')),
                ('max_open_date', models.DateField(null=True, verbose_name='max_open_date')),
                ('camera_type_id', models.IntegerField(null=True, verbose_name='camera_type_id')),
                ('target_keyword', models.CharField(max_length=255, null=True, verbose_name='target_keyword')),
                ('created_at', models.DateTimeField(null=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='updated_at')),
            ],
        ),
    ]
