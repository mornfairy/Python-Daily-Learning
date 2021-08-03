// ��װ������ʾ�ý��棬��void showMenu()
// ��main�����е��÷�װ�õĺ���


#include<iostream>
#include<string>
using namespace std;
#define MAX 1000

//�����ϵ�˽ṹ��,ÿ����ϵ����ͨѶ¼�����洢����Ϣ
struct Person
{
	//����
	string m_Name;
	//�Ա�
	int m_Sex;  // 1����  2��Ů
	//����
	int m_Age;
	//�绰
	string m_Phone;
	//סַ
	string m_Addr;
};

//ͨѶ¼�ṹ��
struct AddressBooks
{
	//ͨѶ¼�б������ϵ�˵�����
	struct Person personArray[MAX];

	//ͨѶ¼�е�ǰ��¼����ϵ�˵ĸ���
	int m_Size;
};

//1�������ϵ��
void addPerson(AddressBooks* abs)
{
	//���ж�ͨѶ¼�Ƿ����������������ټ������
	if (abs->m_Size == MAX)
	{
		cout << "ͨѶ¼�������޷����" << endl;
		return;
	}
	else
	{
		//��Ӿ�����ϵ��

		//����
		string name;
		cout << "����������:" << endl;
		cin >> name;
		abs->personArray[abs->m_Size].m_Name = name;

		//�Ա�
		cout << "�������Ա�" << endl;
		cout << "1 --- ��" << endl;
		cout << "2 --- Ů" << endl;
		int sex = 0;

		while (true)
		{
			//���������1 ���� 2�����˳�ѭ������Ϊ���������ȷֵ
			//�������������������
			cin >> sex;
			if (sex == 1 || sex == 2)
			{
				abs->personArray[abs->m_Size].m_Sex = sex;
				break;
			}
			cout << "������������������" << endl;
		}
		//����
		cout << "���������䣺" << endl;
		int age = 0;
		cin >> age;
		abs->personArray[abs->m_Size].m_Age = age;

		//�绰
		cout << "��������ϵ�绰��" << endl;
		string phone;
		cin >> phone;
		abs->personArray[abs->m_Size].m_Phone = phone;

		//סַ
		cout << "�������ͥ��ַ��" << endl;
		string address;
		cin >> address;
		abs->personArray[abs->m_Size].m_Addr = address;

		//����ͨѶ¼�е�����
		abs->m_Size++;
		cout << "��ӳɹ�" << endl;

		system("pause"); //�밴�������������
		system("cls"); //��������
	}
}

//2����ʾ���е���ϵ��
void showPerson(AddressBooks* abs)
{
	//�ж�ͨѶ¼�������Ƿ�Ϊ0�����Ϊ0����ʾ��¼Ϊ��
	//�����Ϊ0����ʾ��¼����ϵ����Ϣ
	if (abs->m_Size == 0)
	{
		cout << "��ǰ�ļ�¼Ϊ��" << endl;
	}
	else
	{
		for (int i = 0; i < abs->m_Size; i++)
		{
			cout << "����: " << abs->personArray[i].m_Name << "\t";
			cout << "�Ա�: " << (abs->personArray[i].m_Sex == 1 ? "��" : "Ů") << "\t";  //�˴�ʹ����Ŀ���������Ů�Ա�����ж�
			cout << "����: " << abs->personArray[i].m_Age << "\t";
			cout << "�绰: " << abs->personArray[i].m_Phone << "\t";
			cout << "סַ: " << abs->personArray[i].m_Addr << endl;
		}
	}

	system("pause");  // �����������
	system("cls");  // ����
}

//�����ϵ���Ƿ���ڣ�������ڷ�����ϵ���������еľ���λ�ã��粻���ڷ���-1
// ����1  ͨѶ¼  ����2 �Ա�����

int isExist(AddressBooks* abs, string name)
{
	for (int i = 0; i < abs->m_Size; i++)
	{
		//�ҵ��û������������
		if (abs->personArray[i].m_Name == name)
		{
			return i; // �ҵ��Ļ����ͷ���������������е��±���
		}
	}
	return -1; // �������������û���ҵ�������ֵ-1
}

// 3��ɾ����ϵ��
void deletePerson(AddressBooks* abs)
{
	cout << "��������Ҫɾ������ϵ��" << endl;

	string name;
	cin >> name;

	int ret = isExist(abs, name);
	// ret == -1  δ�鵽
	// ret != -1  �鵽��

	if (ret != -1)
	{
		// ���ҵ���Ҫ����ɾ������
		for (int i = ret; i < abs->m_Size; i++)
		{
			// ����ǰ��
			abs->personArray[i] = abs->personArray[i + 1];
		}
		abs->m_Size--;  // ����ͨѶ¼�е���Ա��
		cout << "ɾ���ɹ�" << endl;
	}
	else
	{
		cout << "���޴���" << endl;
	}

	system("pause");
	system("cls");
}

// 4������ָ������ϵ����Ϣ

void findPerson(AddressBooks* abs)
{
	cout << "��������Ҫ���ҵ���ϵ��" << endl;
	string name;
	cin >> name;

	// �ж�ָ������ϵ���Ƿ����
	int ret = isExist(abs, name);

	if (ret != 1) // �ҵ���ϵ��
	{
		cout << "����Ϊ��" << abs->personArray[ret].m_Name << "\t";
		cout << "�Ա�Ϊ��" << abs->personArray[ret].m_Sex << "\t";
		cout << "����Ϊ��" << abs->personArray[ret].m_Age << "\t";
		cout << "�绰Ϊ��" << abs->personArray[ret].m_Phone << "\t";
		cout << "סַΪ��" << abs->personArray[ret].m_Addr << endl;
	}
	else  // δ�ҵ���ϵ��
	{
		cout << "���޴���" << endl;
	}

	// �����������
	system("pause");
	system("cls");
}


// �˵�����
void showMenu()
{
	cout << "***************************" << endl;
	cout << "*****  1�������ϵ��  *****" << endl;
	cout << "*****  2����ʾ��ϵ��  *****" << endl;
	cout << "*****  3��ɾ����ϵ��  *****" << endl;
	cout << "*****  4��������ϵ��  *****" << endl;
	cout << "*****  5���޸���ϵ��  *****" << endl;
	cout << "*****  6�������ϵ��  *****" << endl;
	cout << "*****  0���˳���ϵ��  *****" << endl;
	cout << "***************************" << endl;
}

int main()
{
	//����ͨѶ¼�ṹ�����
	AddressBooks abs;

	//��ʼ��ͨѶ¼�е�ǰ��Ա
	abs.m_Size = 0;

	int select = 0; // �����û�ѡ������ı���


	while (true)
	{
		//��������showMenu()
		showMenu();

		cin >> select;

		switch (select)
		{
		case 1:
			addPerson(&abs);
			break; // 1�������ϵ��

		case 2:
			showPerson(&abs);
			break; // 2����ʾ��ϵ��

		case 3:
			deletePerson(&abs);
			break; // 3��ɾ����ϵ��

		case 4:
			findPerson(&abs);
			break; // 4��������ϵ��

		case 5:; break; // 5���޸���ϵ��
		case 6:; break; // 6�������ϵ��
		case 0:cout << "��ӭ�´�ʹ��" << endl;
			system("pause");
			break; // 0���˳���ϵ��
			return 0;
		default:; break; //
		}
	}

	system("pause");

	return 0;
}