#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> target;
int get_heuristic(vector<vector<int>> src, int depth) {
    int ret = 0;
    for (int i = 0; i < src.size(); i++) {
        for (int j = 0; j < src[i].size(); j++) {
            if (src[i][j] != target[i][j]) {
                ret++;
            }
        }
    }
    return ret + depth;
}
bool check(vector<vector<int>> src) {
    int ret = 0;
    for (int i = 0; i < src.size(); i++) {
        for (int j = 0; j < src[i].size(); j++) {
            if (src[i][j] != target[i][j]) {
                ret++;
                return false;
            }
        }
    }
    return true;
}
struct node {
    vector<vector<int>> Node;
    pair<int, int> zero_index;//0的位置
    string From;//看从什么地方来的 UP DOWN RIGHT LEFT
    int depth{};//递归深度
    node(vector<vector<int>> &Node, pair<int, int> zero, string From, int depth) {
        this->Node = Node;
        this->zero_index = zero;
        this->From = From;
        this->depth = depth;
    }

    node() {}

};
bool operator<(node a1, node a2) {
    if (get_heuristic(a1.Node, a1.depth) == get_heuristic(a2.Node, a2.depth)) {
        if (a1.depth == a2.depth) {
            return a1.From < a2.From;
        }
        return a1.depth > a2.depth;//节点深的排在前面
    } else {
        return get_heuristic(a1.Node, a1.depth) < get_heuristic(a2.Node, a2.depth);
    }

}
pair<int, int> get_zero_index(vector<vector<int>> &a1) {
    for (int i = 0; i < a1.size(); i++) {
        for (int j = 0; j < a1[i].size(); j++) {
            if (a1[i][j] == 0) {
                return {i, j};
            }
        }
    }
}
void print_process(vector<vector<int>> &src, string s) {
    cout << "-----------------------------------------" << endl;
    cout << "The matrix:" << endl;
    for (int i = 0; i < src.size(); i++) {
        for (int j = 0; j < src[i].size(); j++) {
            cout << src[i][j] << "\t";
        }
        cout << endl;
    }
    cout << "has been put in to the" + s << endl;
    cout << "------------------------------------------" << endl;
}
class Eight_Puzzle {
private:
    set<node> Open_List;
    set<node> Close_List;
public:
    Eight_Puzzle() {
    }
    Eight_Puzzle(vector<vector<int>> &src, vector<vector<int>> &tar) {
        target = tar;
        pair<int, int> zero = get_zero_index(src);
        int depth = 0;//初始化深度为0
        node s = node(src, zero, "NULL", depth);
        Open_List.insert(s);
    }
    void solve() {
        node current = *Open_List.begin();
        print_process(current.Node, "Open List");
        while (!check(current.Node)) {
            //当前节点不是目标节点,但可以扩展,放入close表
            Open_List.erase(Open_List.begin());
            print_process(current.Node, "Close List");
            Close_List.insert(current);
            int z_row = current.zero_index.first;
            int z_col = current.zero_index.second;
            int depth = current.depth + 1;//每一个加入深度均要加1
            //提取构造的公共部分
            //first 行标, second 列标
            //向下走
            //1 2 3      1 2 3
            //4 0 5  -> 4 7 5
            //6 7 8      6 0 8
            if (current.From != "UP" && current.zero_index.first + 1 < 3)//判断是不是刚从下面上去
            {
                vector<vector<int>> new_matrix = current.Node;
                swap(new_matrix[z_row][z_col], new_matrix[z_row + 1][z_col]);
                string From = "Down";
                int new_z_row = z_row + 1;
                node p = node(new_matrix, make_pair(new_z_row, z_col), From, depth);
                Open_List.insert(p);//加入open 表
                print_process(new_matrix, "Open List");
            }
            //向上走
            //1 2 3      1 0 3
            //4 0 5  -> 4 2 5
            //6 7 8      6 7 8
            if (current.From != "Down" && current.zero_index.first > 0)//判断是不是刚从上面下来
            {
                vector<vector<int>> new_matrix = current.Node;
                swap(new_matrix[z_row][z_col], new_matrix[z_row - 1][z_col]);
                string From = "UP";
                int new_z_row = z_row - 1;
                node p = node(new_matrix, make_pair(new_z_row, z_col), From, depth);
                Open_List.insert(p);//加入open 表
                print_process(new_matrix, "Open List");
            }
            //向左走
            //1 2 3      1 2 3
            //4 0 5  -> 0 4 5
            //6 7 8      6 7 8
            if (current.From != "Right" && current.zero_index.second > 0)//判断是不是刚从左面来
            {
                vector<vector<int>> new_matrix = current.Node;
                swap(new_matrix[z_row][z_col], new_matrix[z_row][z_col - 1]);
                string From = "Left";
                int new_z_col = z_col - 1;
                node p = node(new_matrix, make_pair(z_row, new_z_col), From, depth);
                Open_List.insert(p);//加入open 表
                print_process(new_matrix, "Open List");
            }
            //向右走
            //1 2 3      1 2 3
            //4 0 5  -> 4 5 0
            //6 7 8      6 7 8
            if (current.From != "Left" && current.zero_index.second + 1 < 3)//判断是不是刚从右面来
            {
                vector<vector<int>> new_matrix = current.Node;
                swap(new_matrix[z_row][z_col], new_matrix[z_row][z_col + 1]);
                string From = "Right";
                int new_z_col = z_col + 1;
                node p = node(new_matrix, make_pair(z_row, new_z_col), From, depth);
                Open_List.insert(p);//加入open 表
                print_process(new_matrix, "Open List");
            }
            current = *Open_List.begin();
        }
        cout << "Success!";
        print_process(current.Node, "Final Node");
    }
};
int main() {
    vector<vector<int>> src(3, vector<int>(3, 0));
    vector<vector<int>> tar(3, vector<int>(3, 0));
    cout << "输入3*3的矩阵src" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> src[i][j];
        }
    }
    cout << "输入3*3的矩阵tar" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cin >> tar[i][j];
        }
    }
    Eight_Puzzle eightPuzzle(src, tar);
    eightPuzzle.solve();
    return 0;
}