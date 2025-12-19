import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knitting_project.settings')
django.setup()

from knitting.models import KnittingPattern, YarnType, Tutorial

# Очистим старые данные
KnittingPattern.objects.all().delete()
YarnType.objects.all().delete()
Tutorial.objects.all().delete()

# Добавим схемы вязания
patterns = [
    KnittingPattern(
        title="Классическая резинка 2x2",
        description="Базовая резинка для манжет и поясов. Идеально подходит для начинающих. Чередование 2 лицевых и 2 изнаночных петель создает эластичное полотно.",
        difficulty="easy",
        yarn_type="Шерсть 100%",
        needle_size="№3-4"
    ),
    KnittingPattern(
        title="Ажурный узор Листья",
        description="Красивый ажурный узор с мотивом листьев. Отлично смотрится на шалях и женских кофточках. Требует внимательности при выполнении накидов.",
        difficulty="medium",
        yarn_type="Мохер или альпака",
        needle_size="№4-5"
    ),
    KnittingPattern(
        title="Сложная коса 8 петель",
        description="Объемная коса из 8 петель с перекрещиванием через 6 рядов. Идеальна для свитеров и кардиганов. Создает роскошную текстуру.",
        difficulty="hard",
        yarn_type="Шерсть или полушерсть",
        needle_size="№4"
    ),
    KnittingPattern(
        title="Платочная вязка",
        description="Самый простой узор - все петли лицевые во всех рядах. Отлично для начинающих и детских вещей. Плотное и теплое полотно.",
        difficulty="easy",
        yarn_type="Любая пряжа",
        needle_size="№3-5"
    ),
    KnittingPattern(
        title="Английская резинка",
        description="Пышная и эластичная резинка с накидами. Используется для шарфов и шапок. Требует больше пряжи, чем обычная резинка.",
        difficulty="medium",
        yarn_type="Акрил или шерсть",
        needle_size="№4"
    ),
]

for pattern in patterns:
    pattern.save()

# Добавим типы пряжи
yarns = [
    YarnType(
        name="Пехорка Кроссбред Бразилии",
        composition="Шерсть 100%",
        thickness="Средняя (200м/100г)",
        price=250.00,
        in_stock=True
    ),
    YarnType(
        name="Alize Lanagold",
        composition="Акрил 51%, Шерсть 49%",
        thickness="Тонкая (240м/100г)",
        price=180.00,
        in_stock=True
    ),
    YarnType(
        name="Nako Mohair Delicate",
        composition="Мохер 40%, Акрил 60%",
        thickness="Тонкая (500м/100г)",
        price=320.00,
        in_stock=False
    ),
    YarnType(
        name="YarnArt Jeans",
        composition="Хлопок 55%, Полиакрил 45%",
        thickness="Средняя (160м/50г)",
        price=85.00,
        in_stock=True
    ),
]

for yarn in yarns:
    yarn.save()

# Добавим уроки
tutorials = [
    Tutorial(
        title="Набор петель классическим способом",
        content="Научитесь правильно набирать петли на спицы. Это основа любого вязания. Классический способ создает прочный край изделия. Подходит для всех типов изделий.",
        video_url="https://www.youtube.com/watch?v=3SVRP5Klo18",
        duration=15
    ),
    Tutorial(
        title="Лицевые и изнаночные петли для начинающих",
        content="Базовые петли в вязании спицами. Разберем технику выполнения лицевых и изнаночных петель, их отличия и применение. После этого урока вы сможете вязать простые узоры.",
        video_url="https://www.youtube.com/watch?v=Lv0U3-0jjmY",
        duration=25
    ),
    Tutorial(
        title="Как читать схемы вязания",
        content="Подробный разбор условных обозначений в схемах. Научитесь читать схемы и превращать их в красивые изделия. Разберем японские и европейские обозначения.",
        video_url="https://www.youtube.com/watch?v=gNXefG39Mzo",
        duration=30
    ),
    Tutorial(
        title="Вязание косы: пошаговая инструкция",
        content="Учимся вязать классическую косу из 6 петель. Подробная инструкция с фотографиями. Узнаете, когда и как перекрещивать петли для создания объемного рельефа.",
        video_url="https://www.youtube.com/watch?v=_qQyzyPYtHw",
        duration=20
    ),
    Tutorial(
        title="Закрытие петель: 3 способа",
        content="Изучите три основных способа закрытия петель: классический, эластичный и декоративный. Каждый способ подходит для разных изделий и создает разный край.",
        video_url="https://www.youtube.com/watch?v=pZkwlELfLq0",
        duration=18
    ),
]

for tutorial in tutorials:
    tutorial.save()

print("✅ Тестовые данные успешно добавлены!")
print(f"Добавлено {len(patterns)} схем вязания")
print(f"Добавлено {len(yarns)} типов пряжи")
print(f"Добавлено {len(tutorials)} уроков")
