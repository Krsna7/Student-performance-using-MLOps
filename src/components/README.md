# Usage of Components

## Data ingestion:
1. We read the data from different components (mongodb, hadoop, etc). Here we used it directly to learn the structure.
2. We make the directory to save the train and test data differently.
3. Saving the data at the directory created
4. Return the data paths.
5. Testing the file

## Data Transformation
1. Make the directory
2. Perform initial transformation like missing values using pipelines for differnet types of data(numerical and categorical).
3. Combine all the transformation pipelines in one transformere variable(preprocessor)
4. return the preprocessor.

5. Preprocess the data.
6. save the file ready to use in the file location created
7. return the path of the train test data.

## Model trainer

1. Split the training and testing data into feature and output.
2. define the models we need to train.
3. extract the best model depending on r2 score or any score metric and return it.




