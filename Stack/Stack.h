#pragma once

class Stack {
	int m_top = -1;
	int m_stack[5];

public:
	int Push(int value);
	int Pop();
	int Peek(int index);
	bool IsEmpty();
	bool IsFull();
	void Warn(const char* message);
	void Print();

};