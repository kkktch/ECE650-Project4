#include "query_funcs.h"

using namespace std;

void add_player(connection *C, int team_id, int jersey_num, string first_name, string last_name,
                int mpg, int ppg, int rpg, int apg, double spg, double bpg)
{
    work W(*C);
    string SQL = "INSERT INTO player (team_id, uniform_num, first_name, last_name, mpg, ppg, rpg, apg, spg, bpg) VALUES ( ";
    SQL += to_string(team_id) + ",";
    SQL += to_string(jersey_num) + ",";
    SQL += W.quote(first_name) + ",";
    SQL += W.quote(last_name) + ",";
    SQL += to_string(mpg) + "," + to_string(ppg) + "," + to_string(rpg) + "," + to_string(apg) + ",";
    SQL += to_string(spg) + "," + to_string(bpg) + ");";
    W.exec(SQL);
    W.commit();
}

void add_team(connection *C, string name, int state_id, int color_id, int wins, int losses)
{
    work W(*C);
    string SQL = "INSERT INTO team (name, state_id, color_id, wins, losses) VALUES ( ";
    SQL += W.quote(name) + ",";
    SQL += to_string(state_id) + "," + to_string(color_id) + "," + to_string(wins) + "," + to_string(losses) + ");";
    W.exec(SQL);
    W.commit();
}

void add_state(connection *C, string name)
{
    work W(*C);
    string SQL = "INSERT INTO state (name) VALUES ( ";
    SQL += W.quote(name) + ");";
    W.exec(SQL);
    W.commit();
}

void add_color(connection *C, string name)
{
    work W(*C);
    string SQL = "INSERT INTO color (name) VALUES ( ";
    SQL += W.quote(name) + ");";
    W.exec(SQL);
    W.commit();
}

void query1(connection *C,
            int use_mpg, int min_mpg, int max_mpg,
            int use_ppg, int min_ppg, int max_ppg,
            int use_rpg, int min_rpg, int max_rpg,
            int use_apg, int min_apg, int max_apg,
            int use_spg, double min_spg, double max_spg,
            int use_bpg, double min_bpg, double max_bpg)
{
    vector<int> use = {use_mpg, use_ppg, use_rpg, use_apg, use_spg, use_bpg};
    vector<string> data = {"mpg", "ppg", "rpg", "apg", "spg", "bpg"};
    vector<double> min = {min_mpg, min_ppg, min_rpg, min_apg, min_spg, min_bpg};
    vector<double> max = {max_mpg, max_ppg, max_rpg, max_apg, max_spg, max_bpg};
    string SQL = "SELECT * FROM player ";
    bool first = false;
    for (int i = 0; i < 6; i++)
    {
        if (use[i])
        {
            if (!first)
            {
                SQL += " WHERE ";
            }
            else
            {
                SQL += " AND ";
            }
            SQL += "(" + to_string(data[i]) + " <= " + to_string(max[i]) + " AND " + to_string(data[i]) + " >= " + to_string(min[i]) + ") ";
            first = true;
        }
    }
    SQL += ";";

    nontransaction NA(*C);
    result R(NA.exec(SQL));
    cout.flags(ios::fixed);
    cout.precision(1);
    cout << "PLAYER_ID TEAM_ID UNIFORM_NUM FIRST_NAME LAST_NAME MPG PPG RPG APG SPG BPG\n";
    for (auto c : R)
    {
        string res_ = to_string(c[0].as<int>()) + " " + to_string(c[1].as<int>()) + " " + to_string(c[2].as<int>()) + " " + c[3].as<string>() + " " + c[4].as<string>() + " ";
        res_ += to_string(c[5].as<int>()) + " " + to_string(c[6].as<int>()) + " " + to_string(c[7].as<int>()) + " " + to_string(c[8].as<int>()) + " ";
        cout << res_ << c[9].as<double>() << " " << c[10].as<double>() << endl;
    }
}

void query2(connection *C, string team_color)
{
    string SQL = "SELECT T.name FROM team as T, color as C WHERE C.name = '";
    SQL += team_color + "' AND C.color_id = T.color_id;";
    nontransaction NA(*C);
    result R(NA.exec(SQL));
    cout << "NAME\n";
    for (auto c : R)
    {
        string res = c[0].as<string>();
        cout << res << endl;
    }
}

void query3(connection *C, string team_name)
{
    string SQL = "SELECT P.first_name, P.last_name FROM player as P, team as T WHERE P.team_id = T.team_id AND T.name = '";
    SQL += team_name + "' ORDER BY P.ppg DESC;";
    nontransaction NA(*C);
    result R(NA.exec(SQL));
    cout << "FIRST_NAME LAST_NAME\n";
    for (auto c : R)
    {
        string res = c[0].as<string>() + " " + c[1].as<string>();
        cout << res << endl;
    }
}

void query4(connection *C, string team_state, string team_color)
{
    string SQL = "SELECT P.first_name, P.last_name, P.uniform_num FROM player as P, team as T, color as C, state as S ";
    SQL += "WHERE P.team_id = T.team_id AND T.color_id = C.color_id AND T.state_id = S.state_id AND S.name = '";
    SQL += team_state + "' AND C.name = '" + team_color + "';";
    nontransaction NA(*C);
    result R(NA.exec(SQL));
    cout << "FIRST_NAME LAST_NAME UNIFORM_NUM\n";
    for (auto c : R)
    {
        string res = c[0].as<string>() + " " + c[1].as<string>() + " " + to_string(c[2].as<int>());
        cout << res << endl;
    }
}

void query5(connection *C, int num_wins)
{
    string SQL = "SELECT P.first_name, P.last_name, T.name, T.wins FROM player as P, team as T WHERE P.team_id = T.team_id AND T.wins > ";
    SQL += to_string(num_wins) + ";";
    nontransaction NA(*C);
    result R(NA.exec(SQL));
    cout << "FIRST_NAME LAST_NAME TEAM_NAME WINS\n";
    for (auto c : R)
    {
        string res = c[0].as<string>() + " " + c[1].as<string>() + " " + c[2].as<string>() + " " + to_string(c[3].as<int>());
        cout << res << endl;
    }
}
