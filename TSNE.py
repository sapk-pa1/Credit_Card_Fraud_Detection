from sklearn.manifold import TSNE
import pandas as pd
tsne = TSNE()
def dim_reduc(x) :
    x_embedded = tsne.fit_transform(x)
    x_embedded_df=pd.DataFrame(x_embedded)
    x_embedded_df.to_csv('reduced.csv',index=None)
    # print(type(x_embedded))