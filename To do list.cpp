#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int perintah;
    vector<string> ListTugas;
    string tugas;
    int JumlahTugas;
    vector<string> status;
    int selesai;
    int JumlahSelesai;
    int JumlahHapus;
    int hapus;
    while (true) {
        cout << "To do list program" << endl;
        cout << "1. Tambah tugas" << endl;
        cout << "2. Lihat tugas" << endl;
        cout << "3. Selesaikan tugas" << endl;
        cout << "4. Hapus tugas" << endl;
        cout << "Masukkan pilihan anda: " << endl;

        cin >> perintah;

        if (perintah == 1) {
            cout << "Masukkan jumlah tugas" << endl;
            cin >> JumlahTugas;
            cout << "Masukkan tugas" << endl;
            for (int i = 0; i < JumlahTugas; i++) {
                cin >> tugas;
                ListTugas.push_back(tugas);
                status.push_back("(Belum selesai)");
            }
        } else if (perintah == 2) {
            for (int i = 0; i < ListTugas.size(); i++) {
                cout << i + 1 << ". " << ListTugas[i] << " " << status[i] << endl;
            }
        } else if (perintah == 3) {
            cout << "Berapa tugas yang ingin di selesaikan" << endl;
            cin >> JumlahSelesai;
            cout << "Pilih tugas yang ingin diselesaikan" << endl;
            for (int i = 0; i < JumlahSelesai; i++) {
                cin >> selesai;
                status[selesai - 1] = "(Sudah selesai)";
            }
        } else {
            cout << "Berapa tugas yang ingin dihapus" << endl;
            cin >> JumlahHapus;
            cout << "Pilih tugas yang ingin dihapus" << endl;
            for (int i = 0; i < JumlahHapus; i++) {
                cin >> hapus;
                hapus -= 1;
                ListTugas.erase(ListTugas.begin() + hapus);
            }
        }
    }
}
