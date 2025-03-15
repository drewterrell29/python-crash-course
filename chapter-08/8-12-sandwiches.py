def build_sandwich(*items):
    """Builds a sandwich"""

    print(f"This is quite the sandwich:")
    for item in items:
        print(item)

build_sandwich("bread", "ham", "cheese")
build_sandwich("bread", "turkey", "mustard", "pickles", "cheese", "sausage")