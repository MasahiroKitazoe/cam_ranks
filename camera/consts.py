from camera.models import Finder, Maker


def create_model_choices(model):
    choices = [(None, "--------")]
    for instance in model.objects.all():
        choices.append((instance.id, instance.choice_name()))
    return tuple(choices)


SHUTTER_SPEED = (
    (None, "--------"),
    (30, "30秒"),
    (25, "25秒"),
    (20, "20秒"),
    (15, "15秒"),
    (13, "13秒"),
    (10, "10秒"),
    (8, "8秒"),
    (6, "6秒"),
    (5, "5秒"),
    (4, "4秒"),
    (3.2, "3.2秒"),
    (2.5, "2.5秒"),
    (2, "2秒"),
    (1.6, "1.3秒"),
    (1, "1秒"),
    (0.8, "0.8秒"),
    (0.6, "0.6秒"),
    (0.5, "0.5秒"),
    (0.4, "0.4秒"),
    (1/3, "1/3秒"),
    (1/4, "1/4秒"),
    (1/5, "1/5秒"),
    (1/6, "1/6秒"),
    (1/8, "1/8秒"),
    (1/10, "1/10秒"),
    (1/13, "1/13秒"),
    (1/15, "1/15秒"),
    (1/20, "1/20秒"),
    (1/25, "1/25秒"),
    (1/30, "1/30秒"),
    (1/40, "1/40秒"),
    (1/50, "1/50秒"),
    (1/60, "1/60秒"),
    (1/80, "1/80秒"),
    (1/100, "1/100秒"),
    (1/125, "1/125秒"),
    (1/160, "1/160秒"),
    (1/200, "1/200秒"),
    (1/250, "1/250秒"),
    (1/320, "1/320秒"),
    (1/400, "1/400秒"),
    (1/500, "1/500秒"),
    (1/640, "1/640秒"),
    (1/800, "1/800秒"),
    (1/1000, "1/1000秒"),
    (1/1250, "1/1250秒"),
    (1/1600, "1/1600秒"),
    (1/2000, "1/2000秒"),
    (1/2500, "1/2500秒"),
    (1/3200, "1/3200秒"),
    (1/4000, "1/4000秒"),
    (1/5000, "1/5000秒"),
    (1/6400, "1/6400秒"),
    (1/8000, "1/8000秒"),
    (1/10000, "1/10000秒"),
)

F_VALUE = (
    (None, "--------"),
    (1.4, "1.4"),
    (2.0, "2.0"),
    (2.8, "2.8"),
    (4.0, "4.0"),
    (5.6, "5.6"),
    (8.0, "8.0"),
    (11, "11"),
    (16, "16"),
    (22, "22"),
    (32, "32"),
)

BOOLEAN = ((None, "--------"), (True, "○"), ("", "なし"))

CAMERA_TYPE_CHOICES = (
    (None, "--------"),
    (1, "コンデジ"),
    (2, "ミラーレス一眼"),
    (3, "一眼レフ")
)

FRAME_CHOICES = (
    (None, "--------"),
    (1, "中判サイズ"),
    (2, "フルサイズ"),
    (3, "APS-C"),
    (4, "4/3型"),
    (5, "1型"),
    (6, "1/2.3型"),
    (7, "1/3.1型"),
    (8, "1/1.7型"),
    (9, "1.5型"),
    (10, "1/10型"),
    (11, "1/5型"),
)

# ファインダーとメーカーは増える可能性があるので、動的に指定
FINDER_CHOICES = create_model_choices(Finder)

MAKER_CHOICES = create_model_choices(Maker)
