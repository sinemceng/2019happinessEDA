import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_veri():
    df = pd.read_csv("veri.csv")
    #readme dosyasında belirttiğim bağlantıdan veri setine ulaşabilirsiniz.
    print(df.head(5))
    print("\nInfo")
    print(df.info())
    print("\nDescribe")
    print(df.describe())
    print()
    return df

def null_control(df):
    print("Null Control")
    print(df.isnull().sum())
    print()

def heatmap(df):
    fig=plt.figure(figsize=(12,7))
    fig=sns.heatmap(df.isnull(), cbar=True, cmap="viridis")
    plt.title("Eksik Veri Haritası")
    plt.tight_layout()
    plt.savefig("heatmap", dpi=200, bbox_inches="tight")
    plt.show()

def types(df):
    print(df.dtypes)
    print()

def std_var(df):
    columns = ["Score", "GDP per capita", "Social support",
               "Healthy life expectancy", "Freedom to make life choices",
               "Generosity", "Perceptions of corruption"]
    print()
    for col in columns:
        std=df[col].std()
        var=df[col].var()
        print(f"{col} Standart Sapma: {std:.2f} Varyans: {var:.2f} ")
    print()

def string_dagilim(df):
    fig=plt.figure(figsize=(20,5))
    #Kategorik değişkenlerin dağılımı
    categorical=df.select_dtypes(include="object").columns
    for col in categorical:
      print(df[col].value_counts())
      fig=sns.countplot(data=df,x=col)
      plt.title(f"{col} Sütunun Dağılımı")
      plt.xticks(rotation=45)
      plt.tight_layout()
      plt.savefig("string.png", dpi=200, bbox_inches="tight")
      plt.show()

def hist(df):
    numeric_cols = df.select_dtypes(include=np.number).columns
    num_cols = len(numeric_cols)

    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12,7))
    axes = axes.flatten()
    for i, col in enumerate(numeric_cols):
        sns.histplot(df[col], kde=True, ax=axes[i], color="red")
        axes[i].set_title(f"{col} Dağılımı",fontdict={"family":"serif","color":"darkblue","size":12})
        axes[i].set_xlabel(col)
        axes[i].set_ylabel("Frekans")

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.suptitle("Her Özellik için Ayrı HistPlot", fontsize=16, y=1.0)
    plt.subplots_adjust(top=0.9)
    plt.savefig("histplot.png",dpi=200,bbox_inches="tight")
    plt.show()

def plot_(df):
    columns = ["Score", "GDP per capita", "Social support",
               "Healthy life expectancy", "Freedom to make life choices",
               "Generosity", "Perceptions of corruption"]

    fig,axes=plt.subplots(nrows=3, ncols=3, figsize=(12,7))
    axes=axes.flatten()
    for i, column in enumerate(columns):
      df[column].plot(kind="hist",alpha=0.7,ax=axes[i],color="darkblue")
      font1={"family": "serif","color":"darkred","size":15}
      axes[i].set_title(column,fontdict=font1)
      axes[i].set_xlabel("Değer")
      axes[i].set_ylabel("Frekans")

    for j in range(len(columns), len(axes)):
      fig.delaxes(axes[j])

    plt.tight_layout()
    plt.suptitle("Her Özellik için Ayrı Histogramlar", fontsize=16, y=1.0)
    plt.subplots_adjust(top=0.9)
    plt.savefig("plot.png", dpi=200, bbox_inches="tight")
    plt.show()

def box(df):

    columns = ["Score", "GDP per capita", "Social support",
               "Healthy life expectancy", "Freedom to make life choices",
               "Generosity", "Perceptions of corruption"]

    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12,7))
    axes = axes.flatten()

    for i, column in enumerate(columns):
        axes[i].boxplot(df[column], vert=True)
        axes[i].set_title(column,fontdict={"family":"serif","color":"darkblue","size":12})
        axes[i].set_ylabel("Notlar")

    for j in range(len(columns), len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.suptitle("Her Özellik için Ayrı Box Plotlar", fontsize=13, y=1.0)
    plt.savefig("box.png", dpi=200, bbox_inches="tight")
    plt.show()

def heat(df):
    plt.figure(figsize=(10, 15))
    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Korelasyon Matrisi")
    plt.tight_layout()  # Alt grafiklerin yerleşimini düzeltir
    plt.subplots_adjust(top=0.95)  # Başlık ile grafik arasındaki boşluğu azaltır
    plt.savefig("heat.png", dpi=200, bbox_inches="tight")
    plt.show()

def main():
    df=load_veri()
    null_control(df)
    heatmap(df)
    types(df)
    std_var(df)
    string_dagilim(df)
    hist(df)
    plot_(df)
    box(df)
    heat(df)

if __name__== "__main__":
    main()