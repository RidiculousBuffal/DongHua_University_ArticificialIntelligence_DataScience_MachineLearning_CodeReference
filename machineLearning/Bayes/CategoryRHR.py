from collections import Counter, defaultdict


class NaiveBayesClassifier:
    def __init__(self, smooth=1):
        self.smooth = smooth
        self.conditional_p = defaultdict(dict)
        self.y_p = {}

    def fit(self, X, y):
        if self.smooth == 1:
            print("using Laplace smoothing")
        else:
            print("Using normal method")

        y_counts = dict(Counter(y))
        print("The separating of Y:", y_counts)

        # Determine unique values for each feature
        unique_values_per_feature = [set(features) for features in zip(*X)]

        for key in y_counts:
            y_filtered = [(features, label) for features, label in zip(X, y) if label == key]
            for i, _ in enumerate(unique_values_per_feature):
                feature_values = [features[i] for features, _ in y_filtered]
                feature_counts = dict(Counter(feature_values))
                Len_Of_Current_X = len(unique_values_per_feature[i])
                for feature_value, count in feature_counts.items():
                    prob = (count + self.smooth) / (y_counts[key] + Len_Of_Current_X * self.smooth)
                    self.conditional_p[key][str(feature_value)] = prob

        len_y = len(y)
        count_y = len(y_counts)
        for key in y_counts:
            self.y_p[key] = (y_counts[key] + self.smooth) / (len_y + count_y * self.smooth)

    def predict(self, X_test):
        print("Starting predict:")
        predictions = []
        for features in X_test:
            max_prob = -1
            winner = None
            for key, prior in self.y_p.items():
                prob = prior
                for i, feature_value in enumerate(features):
                    prob *= self.conditional_p[key].get(str(feature_value), 0)
                print(f"PROB OF {key} IS{prob}")
                if prob > max_prob:
                    max_prob = prob
                    winner = (key, prob)
            predictions.append(winner)
        return predictions


if __name__ == '__main__':
    data = [
        (1, 'S', -1), (1, 'M', -1), (1, 'M', 1), (1, 'S', 1),
        (1, 'S', -1), (2, 'S', -1), (2, 'M', -1), (2, 'M', 1),
        (2, 'L', 1), (2, 'L', 1), (3, 'L', 1), (3, 'M', 1),
        (3, 'M', 1), (3, 'L', 1), (3, 'L', -1)
    ]

    # Separating features and labels
    X_train = [(x1, x2) for x1, x2, _ in data]
    Y_train = [y for _, _, y in data]

    classifier = NaiveBayesClassifier(smooth=1)
    classifier.fit(X_train, Y_train)

    X_test = [(2, 'S')]
    predictions = classifier.predict(X_test)
    print("result:", predictions)
