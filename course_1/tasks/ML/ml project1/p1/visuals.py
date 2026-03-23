###########################################
# Suppress matplotlib user warnings
from pyexpat import features
import warnings
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve, ShuffleSplit, train_test_split, validation_curve
from sklearn.tree import DecisionTreeRegressor

warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
warnings.filterwarnings("ignore")


def ModelComplexity(X, y):
    """ Calculates the performance of the model as model complexity increases.
        The learning and testing error rates are then plotted.
        
        :param X: features
        :type X: numpy array
        :param y: target variable
        :type y: numpy array

        :return: None
        :rtype: None
        """

    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

    # Vary the max_depth parameter from 1 to 10
    max_depth = np.arange(1, 11)

    # Calculate the training and testing scores
    train_scores, test_scores = validation_curve(
        DecisionTreeRegressor(), X, y,
        param_name="max_depth",
        param_range=max_depth,
        cv=cv,
        scoring='r2'
    )

    # Find the mean and standard deviation for smoothing
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    # Plot the validation curve
    plt.figure(figsize=(7, 5))
    plt.title('Decision Tree Regressor Complexity Performance')
    plt.plot(max_depth, train_mean, 'o-', color='r', label='Training Score')
    plt.plot(max_depth, test_mean, 'o-', color='g', label='Validation Score')
    plt.fill_between(max_depth, train_mean - train_std,
                     train_mean + train_std, alpha=0.15, color='r')
    plt.fill_between(max_depth, test_mean - test_std,
                     test_mean + test_std, alpha=0.15, color='g')

    # Visual aesthetics
    plt.legend(loc='lower right')
    plt.xlabel('Maximum Depth')
    plt.ylabel('Score')
    plt.ylim([-0.05, 1.05])
    plt.tight_layout()
    plt.savefig('complexity_curve.png', dpi=100, bbox_inches='tight')
    plt.show()
    print("✅ Complexity curve saved as 'complexity_curve.png'")


def ModelLearning(X, y):
    """ Calculates the performance of several models with varying sizes of training data.
       The learning and testing scores for each model are then plotted. 
        
        :param X: features
        :type X: numpy array
        :param y: target variable
        :type y: numpy array
        
        :return: None
        :rtype: None
        """
    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

    # Generate the training set sizes increasing by 50
    train_sizes = np.rint(np.linspace(1, X.shape[0] * 0.8 - 1, 9)).astype(int)

    # Create the figure window
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))

    # Create four different models based on max_depth
    for k, depth in enumerate([1, 3, 6, 10]):
        regressor = DecisionTreeRegressor(max_depth=depth)

        sizes, train_scores, test_scores = learning_curve(
            regressor, X, y, cv=cv, train_sizes=train_sizes, scoring='r2'
        )

        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)

        ax = axes[k // 2, k % 2]
        ax.plot(sizes, train_mean, 'o-', color='r', label='Training Score')
        ax.plot(sizes, test_mean, 'o-', color='g', label='Testing Score')
        ax.fill_between(sizes, train_mean - train_std, train_mean + train_std, alpha=0.15, color='r')
        ax.fill_between(sizes, test_mean - test_std, test_mean + test_std, alpha=0.15, color='g')

        ax.set_title(f'max_depth = {depth}')
        ax.set_xlabel('Number of Training Points')
        ax.set_ylabel('Score')
        ax.set_xlim([0, X.shape[0] * 0.8])
        ax.set_ylim([-0.05, 1.05])
        ax.legend(loc='lower right')

    fig.suptitle('Decision Tree Regressor Learning Performances', fontsize=16, y=1.03)
    fig.tight_layout()
    plt.savefig('learning_curves.png', dpi=100, bbox_inches='tight')
    plt.show()
    print("✅ Learning curves saved as 'learning_curves.png'")


def PredictTrials(X, y, fitter, data):
    """ Performs trials of fitting and predicting data. 

        :param X: features
        :type X: numpy array
        :param y: target variable
        :type y: numpy array
        :param fitter: function that fits a model to the data
        :type fitter: function
        :param data: data point to predict
        :type data: list or numpy array 

        :return: None   
        :rtype: None    

    """

    prices = []

    for k in range(10):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=k
        )

        reg = fitter(X_train, y_train)
        pred = reg.predict([data[0]])[0]
        prices.append(pred)

        print('Trial {}: ${:,.2f}'.format(k + 1, pred))

    print('\nRange in prices: ${:,.2f}'.format(max(prices) - min(prices)))
