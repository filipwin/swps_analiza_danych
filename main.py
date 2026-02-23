import pandas as pd
import polars as pl


sales = [
    {"date":"2026-01-02","city":"Warszawa","category":"Kawa","product":"Espresso","qty":3,"price":12.0,"payment":"card"},
    {"date":"2026-01-02","city":"Warszawa","category":"Kawa","product":"Latte","qty":2,"price":16.0,"payment":"cash"},
    {"date":"2026-01-03","city":"Kraków","category":"Herbata","product":"Earl Grey","qty":1,"price":11.0,"payment":"card"},
    {"date":"2026-01-03","city":"Gdańsk","category":"Kawa","product":"Cappuccino","qty":2,"price":15.0,"payment":"card"},
    {"date":"2026-01-04","city":"Kraków","category":"Ciasto","product":"Sernik","qty":1,"price":18.0,"payment":"cash"},
    {"date":"2026-01-04","city":"Warszawa","category":"Ciasto","product":"Brownie","qty":2,"price":14.0,"payment":"card"},
    {"date":"2026-01-05","city":"Gdańsk","category":"Herbata","product":"Matcha","qty":1,"price":19.0,"payment":"card"},
    {"date":"2026-01-05","city":"Warszawa","category":"Kawa","product":"Latte","qty":1,"price":16.0,"payment":"card"},
    {"date":"2026-01-06","city":"Kraków","category":"Kawa","product":"Espresso","qty":2,"price":12.0,"payment":"cash"},
    {"date":"2026-01-06","city":"Gdańsk","category":"Ciasto","product":"Sernik","qty":1,"price":18.0,"payment":"card"},
]


def zad1_pandas():
    print("\n### ZAD 1 ###")
    df = pd.DataFrame(sales)

    print("=== head() ===")
    print(df.head())
    print()

    print("=== info() ===")
    df.info()
    print()

    print("=== describe() ===")
    print(df.describe())
    print()

    rows, cols = df.shape
    print(f"Liczba wierszy: {rows}")
    print(f"Liczba kolumn: {cols}")


def zad1_polars():
    print("\n### ZAD 1 ###")
    df = pl.DataFrame(sales)

    print("=== head() ===")
    print(df.head())
    print()

    print("=== describe() ===")
    print(df.describe())
    print()

    print("=== info() ===")
    # Zdaje sie ze Polars nie ma info(). Czesc tych informacji mozna uzyskac za pomoca schema, estimated_size i describe
    print(f"Struktura: {df.schema}")
    print(f"Rozmiar: {df.estimated_size()}")

    rows, cols = df.shape
    print(f"\nLiczba wierszy: {rows}")
    print(f"Liczba kolumn: {cols}")


def zad2_pandas():
    print("\n### ZAD 2 ###")
    df = pd.DataFrame(sales)
    df["value"] = df["qty"] * df["price"]
    df = df.sort_values("value", ascending=False)
    print(df)


def zad2_polars():
    print("\n### ZAD 2 ###")
    df = pl.DataFrame(sales)
    df = df.with_columns(
        (pl.col("qty") * pl.col("price")).alias("value")
    ).sort("value", descending=True)
    print(df)


def main():
    print("\n" + ("=" * 30) + " PANDAS " + ("=" * 30) + "\n")
    zad1_pandas()
    zad2_pandas()
    print("\n" + ("=" * 30) + " POLARS " + ("=" * 30) + "\n")
    zad1_polars()
    zad2_polars()


if __name__ == "__main__":
    main()
