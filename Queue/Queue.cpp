#include <iostream>
#include "Queue.h"

using namespace std;


bool Queue::IsEmpty() {
	return m_front == m_rear;
}

bool Queue::IsFull() {
	return m_rear >= 4;
}


int Queue::Enqueue(int value) {
	if (IsFull()) {
		Warn("Queue is Full");
		return value;
	}
	if (IsEmpty()) {
		m_front = m_rear = 0;
	}
	m_queue[m_rear] = value;
	m_rear++;
	return value;
}

int Queue::Dequeue() {
	int removedValue;
	if (IsEmpty()) {
		Warn("Queue is Empty");
		return -1;
	}
	removedValue = m_queue[m_front];
	m_queue[m_front] = 0;
	m_front++;
	return removedValue;
}

void Queue::Print() {
	for (int c = 0; c < m_rear; c++) {
		cout << "[" << c << "]" << m_queue[c] << endl;
	}
}

void Queue::Warn(const char* message) {
	cout << "[WARN]" << message << endl;
}

int Queue::Peek(int index) {
	return m_queue[index];
}