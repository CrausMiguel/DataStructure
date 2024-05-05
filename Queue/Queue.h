#pragma once

class Queue {
	int m_front = -1;
	int m_rear = -1;
	int m_queue[5];

public:
	int Enqueue(int value);
	int Dequeue();
	int Peek(int index);
	bool IsEmpty();
	bool IsFull();
	void Warn(const char* message);
	void Print();

};