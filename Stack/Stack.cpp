#include "Stack.h"
#include <iostream>    

using namespace std;

bool Stack::IsEmpty() {
	return m_top < 0;
}

bool Stack::IsFull() {
	return m_top >= 4;
}

int Stack::Push(int value) {
	if (IsFull()) {
		Warn("Stack is full");
		return value;
	}
	m_top++;
	m_stack[m_top] = value;
	return value;
}

int Stack::Pop() {
	int removedValue;
	if (IsEmpty()) {
		Warn("Stack if Empty");
		return -1;
	}
	removedValue = m_stack[m_top];
	m_stack[m_top] = 0;
	m_top--;
	return removedValue;
}

void Stack::Print() {
	for (int c = 0; c <= m_top; c++) {
		cout << "[" << c << "]" << m_stack[c] << endl;
	}
}

void Stack::Warn(const char* message) {
	cout << "[WARN]" << message << endl;
}

int Stack::Peek(int index) {
	return m_stack[index];
}