from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
import utils.eda as eda

reader = Reader(rating_scale=(0, 10))
data = Dataset.load_from_df(eda.ratings, reader)

model = SVD()
cross_validate(model, data, cv=5, verbose=True)