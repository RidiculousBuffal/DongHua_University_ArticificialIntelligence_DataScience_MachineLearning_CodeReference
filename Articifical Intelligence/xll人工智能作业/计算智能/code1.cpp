#include <vector>
#include <iostream>

using namespace std;

//重载向量加法:
pair<double, double> operator+(pair<double, double> d1, pair<double, double> d2) {
    return make_pair(d1.first + d2.first, d1.second + d2.second);
}

//重载数乘:
pair<double, double> operator*(double k, pair<double, double> d1) {
    return {k * d1.first, k * d1.second};
}

pair<double, double> operator*(int k, pair<double, double> d1) {
    return {k * d1.first, k * d1.second};
}

double operator*(pair<double, double> d1, pair<double, double> d2) {
    return d1.first * d2.first + d1.second * d2.second;
}

//减法
pair<double, double> operator-(pair<double, double> d1, pair<double, double> d2) {
    return {d1.first - d2.first, d1.second - d2.second};
}

struct train_set {
    pair<double, double> X_1_X_2;
    int y;

    train_set(const pair<double, double> &x1X2, int y) : X_1_X_2(x1X2), y(y) {}
};

struct test_set {
    pair<double, double> X_1_X_2;

    test_set(const pair<double, double> &x1X2) : X_1_X_2(x1X2) {}
};

class Single_Layer_Perceptron {
private:
    pair<double, double> w1_w2;
    double b = 0;
    double eta = 0;//学习常数
    vector<train_set> trainset;
public:
    Single_Layer_Perceptron(vector<train_set> W1W2, double eta = 1, double b = 0) {
        this->b = b;
        this->eta = eta;
        double x1_P = 0;//正例中的x1
        double x2_P = 0;//正例中的x2
        double x1_N = 0;//反例中的x1
        double x2_N = 0;//反例中的x2
        //1是正,0是反
        for (train_set ts: W1W2) {
            if (ts.y == 0) {
                //反例
                x1_N += ts.X_1_X_2.first;
                x2_N = ts.X_1_X_2.second;
            } else {
                x1_P += ts.X_1_X_2.first;
                x2_P = ts.X_1_X_2.second;
            }
        }
        w1_w2 = make_pair(x1_P - x2_P, x1_N - x2_N);
        this->trainset = W1W2;
    }

    int get_result(pair<double, double> d1) {
        double result = w1_w2 * d1 + b;
        if (result < 0) {
            return 0;
        } else {
            return 1;
        }
    }

    void print_result(vector<test_set> testSet) {
        for (test_set ts: testSet) {
            cout << "The test case:(" << ts.X_1_X_2.first << "," << ts.X_1_X_2.second << ")" << "'s result is "
                 << get_result(ts.X_1_X_2) << endl;
        }
    }

    bool check_ok(vector<train_set> trainSet) {
        for (train_set ts: trainSet) {
            if (get_result(ts.X_1_X_2) != ts.y) {
                return false;
            }
        }
        return true;
    }

    void fit() {
        int i = 0;
        while (!check_ok(trainset)) {
            cout << "Now it is the " << i << "th training!" << endl;
            for (train_set ts: trainset) {
                w1_w2 = w1_w2 + eta * (ts.y - get_result(ts.X_1_X_2)) * ts.X_1_X_2;
            }
            cout << "now: w1 =" << w1_w2.first << ",w2=" << w1_w2.second << ",b=" << b << endl;
            i++;
        }

    }

};

int main() {
    vector<train_set> trainset;
    trainset.push_back({{-9, 15}, 0});
    trainset.push_back({{1, 8}, 1});
    trainset.push_back({{-12, 4}, 0});
    trainset.push_back({{-4, 5}, 0});
    trainset.push_back({{0, 11}, 0});
    trainset.push_back({{5, 9}, 1});
    Single_Layer_Perceptron slp = Single_Layer_Perceptron(trainset);
    slp.fit();
    cout << "fitting end! ..................................." << endl;
    vector<test_set> ts;
    ts.push_back({{2, -5}});
    ts.push_back({{-10, 10}});
    ts.push_back({{0, 5}});
    ts.push_back({{-6, 6}});
    slp.print_result(ts);
    return 0;
}