#include <vector>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;
struct Rules {
    string Evidence;
    string Hypothesis;
    long double LS;
    long double LN;

    Rules(const string &evidence, const string &hypothesis, long double ls, long double ln)
            : Evidence(evidence), Hypothesis(hypothesis), LS(ls), LN(ln) {}

    void print() {
        printf("IF %s THEN (%lf,%lf) %s \n", Evidence.c_str(), LS, LN, Hypothesis.c_str());
    }

    pair<long double, long double> get_LS_LN() {
        return {LS, LN};
    }
};
vector<Rules> input_Rules() {
    //输入数据
    vector<Rules> res;
    long double LS, LN;
    cout << "Input LS1 and LN1 for E1 and H1" << endl;
    cin >> LS >> LN;
    res.push_back({"E1", "H1", LS, LN});
    res[0].print();
    cout << "Input LS2 and LN2 for E2 and H1" << endl;
    cin >> LS >> LN;
    res.push_back({"E2", "H1", LS, LN});
    res[1].print();
    cout << "Input LS3 and LN3 for H1 and H2" << endl;
    cin >> LS >> LN;
    res.push_back({"H1", "H2", LS, LN});
    res[2].print();
    cout << "Input LS4 and LN4 for E3 and H2" << endl;
    cin >> LS >> LN;
    res.push_back({"E3", "H2", LS, LN});
    res[3].print();
    return res;
}
vector<long double> input_OH() {
    long double OH;
    vector<long double> res;
    cout << "Now input O(H1)" << endl;
    cin >> OH;
    res.push_back(OH);
    cout << "Now input O(H2)" << endl;
    cin >> OH;
    res.push_back(OH);
    return res;
}
vector<long double> input_C_ES() {
    long double C_ES;
    vector<long double> res;
    for (int i = 1; i <= 3; i++) {
        printf("Now input C(E%d|S%d)\n", i, i);
        cin >> C_ES;
        res.push_back(C_ES);
    }
    return res;
}
class My_Bayes {
private:
    vector<Rules> rules;
    vector<long double> OH;//O(H1),O(H2)...
    vector<long double> C_ES;//C(E1|S1),C(E2|S2)....
public:
    My_Bayes() {
        this->rules = input_Rules();
        this->OH = input_OH();
        this->C_ES = input_C_ES();
    }

    pair<long double, long double> Get_P_E_H_and_P_E_not_H(long double LS, long double LN) {
        long double P_E_H = LS * (LN - 1) / (LN - LS);
        long double P_E_NOT_H = (LN - 1) / (LN - LS);
        return {P_E_H, P_E_NOT_H};
    }//通过LS|LN的二元方程拿到P(E|H)和P(E|~H)
    long double From_O_get_P(long double O) {
        return O / (1 + O);
    }

    long double get_Not(long double P) {
        return 1 - P;//P(A)→P(~A)
    }

    long double From_P_get_O(long double P) {
        return P / (1 - P);
    }

    long double get_P_E_from_Bayes_basic_formula(long double P_EH, long double P_H, long double P_HE) {
        return P_EH * P_H / P_HE;
    }

    long double get_P_HE(long double P_EH, long double P_H, long double P_E) {
        return P_EH * P_H / P_E;
    }

    long double get_P_NotH_E(long double P_E_NotH, long double P_NotH, long double P_E) {
        return P_E_NotH * P_NotH / P_E;
    }

    pair<long double, long double> Updated_Bayes_O_HE_O_H_Not_E(pair<long double, long double> LS_LN, long double O_H) {
        //拿到O(H|E),O(H|~E);
        long double O_H_E = LS_LN.first * O_H;
        long double O_H_NotE = LS_LN.second * O_H;
        return {O_H_E, O_H_NotE};
    }

    long double get_P_ES(long double C_ES, long double P_E) {
        if (0 <= C_ES && C_ES <= 5) {
            return (C_ES + P_E * (5 - C_ES)) / 5;
        } else if (-5 <= C_ES && C_ES <= 0) {
            return (P_E * (C_ES + 5)) / 5;
        } else {
            cout << "ERROR C(E|S)" << endl;
            exit(0);
        }
    }

    long double get_C_ES(long double P_ES, long double P_E) {
        if (P_E <= P_ES && P_ES <= 1) {
            return 5 * (P_ES - P_E) / (1 - P_E);
        } else if (0 <= P_ES && P_ES <= P_E) {
            return 5 * (P_ES - P_E) / P_E;
        } else {
            cout << "ERROR P(E|S)" << endl;
            exit(0);
        }
    }

    long double
    get_P_HS_from_Duda_Original(long double P_HE, long double P_ES, long double P_H_NotE, long double P_NotE_S) {
        return P_HE * P_ES + P_H_NotE * P_NotE_S;
    }

    long double
    get_P_HS_from_EH_Linear_Interpolation(long double P_H, long double P_E, long double P_ES, long double P_HE,
                                          long double P_H_not_E) {
        if (0 <= P_ES && P_ES < P_E) {
            return P_H_not_E + ((P_H - P_H_not_E) / P_E) * P_ES;
        } else if (P_E <= P_ES && P_ES <= 1) {
            return P_H + ((P_HE - P_H) / (1 - P_E)) * (P_ES - P_E);
        } else {
            cout << "ERROR P(E|S)" << endl;
            exit(0);
        }
    }

    long double get_P_HS_From_CP_formula(long double P_H, long double P_HE, long double P_H_NotE, long double C_ES) {
        if (C_ES <= 0) {
            return P_H_NotE + (P_H - P_H_NotE) * ((1 / 5.0) * C_ES + 1);
        } else {
            return P_H + (P_HE - P_H) * (1 / 5.0) * C_ES;
        }
    }

    long double Get_Posterior_Probability_From_All_Observation(vector<long double> O_HS, long double O_H) {
        long double multi = 1;
        for (long double res: O_HS) {
            multi = multi * (res / O_H);
        }
        return multi * O_H;
    }

    long double process_O_H_S(int index_H, int index_RULE, int index_C)//采用1,2,3,4的下标输入
    {
        index_RULE = index_RULE - 1;
        index_H = index_H - 1;
        index_C = index_C - 1;
        long double P_H = From_O_get_P(OH[index_H]);
        cout << "P_H" << index_H+1 << "=" << P_H<<endl;
//        cout<<P_H<<endl;
        //get O(H1|E1)
        long double O_H_E = Updated_Bayes_O_HE_O_H_Not_E(rules[index_RULE].get_LS_LN(), OH[index_H]).first;
        //get P(H1|E1) and P(H1|~E1)
        long double P_H_E = From_O_get_P(O_H_E);
//        cout<<P_H_E<<endl;
        long double O_H_NotE = Updated_Bayes_O_HE_O_H_Not_E(rules[index_RULE].get_LS_LN(), OH[index_H]).second;
        long double P_H_NotE = From_O_get_P(O_H_NotE);
        //get P(H1|S1)
        long double P_H_S = get_P_HS_From_CP_formula(P_H, P_H_E, P_H_NotE, C_ES[index_C]);
        //get O(H1|S1)
        long double O_H_S = From_P_get_O(P_H_S);
        return O_H_S;
    }

    long double solve_question() {
        //cal O(H1|S1)
        long double O_H1_S1 = process_O_H_S(1, 1, 1);
        cout << "O_H1_S1=" << O_H1_S1 << endl;
        //cal O(H2|S2)
        long double O_H1_S2 = process_O_H_S(1, 2, 2);
        cout << "O_H1_S2=" << O_H1_S2 << endl;
        //cal O(H1|S1S2)
        long double O_H1_S1S2 = Get_Posterior_Probability_From_All_Observation({O_H1_S1, O_H1_S2}, OH[0]);
        cout << "O_H1_S1S2=" << O_H1_S1S2 << endl;
        //cal O(H2|S1S2)
        //cal P(H2)
        long double O_H2 = OH[1];
        long double P_H2 = From_O_get_P(O_H2);
        cout << "P_H2=" << P_H2 << endl;
        //cal P(H1|S1S2)
        long double P_H1_S1S2 = From_O_get_P(O_H1_S1S2);
        cout << "P_H1_S1S2=" << P_H1_S1S2 << endl;
        //cal P(H2|H1)
        //cal O(H2|H1)
        long double O_H2_H1 = Updated_Bayes_O_HE_O_H_Not_E(rules[2].get_LS_LN(), O_H2).first;
        cout << "O_H2_H1 =" << O_H2_H1 << endl;
        long double O_H2_NotH1 = Updated_Bayes_O_HE_O_H_Not_E(rules[2].get_LS_LN(), O_H2).second;
        long double P_H2_H1 = From_O_get_P(O_H2_H1);
        cout << "P_H2_H1=" << P_H2_H1 << endl;
        long double P_H2_NotH1 = From_O_get_P(O_H2_NotH1);
        //CAL P(H2|S1S2)
        //h1是h2的证据
        //cal P(h1)
        long double P_H1 = From_O_get_P(OH[0]);
        long double P_H2_S1S2 = get_P_HS_from_EH_Linear_Interpolation(P_H2, P_H1, P_H1_S1S2, P_H2_H1, P_H2_NotH1);
        cout << "P_H2_S1S2=" << P_H2_S1S2 << endl;
        //cal O(H2|S1S2)2
        long double O_H2_S1S2 = From_P_get_O(P_H2_S1S2);
        cout << "O_H2_S1S2=" << O_H2_S1S2 << endl;
        //cal O(H2|S3) h2,rule4 c(e3|s3)
        long double O_H2_S3 = process_O_H_S(2, 4, 3);
        cout << "O_H2_S3=" << O_H2_S3 << endl;
        //cal O(H2|S1S2S3)
        long double O_H2_S1S2S3 = Get_Posterior_Probability_From_All_Observation({O_H2_S1S2, O_H2_S3}, O_H2);
        cout << "--------------------------------------------------------------" << endl;
        cout << "O_H2_S1S2S3=" << O_H2_S1S2S3 << endl;
        cout << "--------------------------------------------------------------" << endl;
        return O_H2_S1S2S3;

    }
};
int main() {
    My_Bayes myBayes = My_Bayes();
    myBayes.solve_question();
    return 0;
}