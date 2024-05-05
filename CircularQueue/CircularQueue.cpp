#include "CircularQueue.h"
#include <array>
#include <iostream>

using namespace std;


bool CircularQueue::IsEmpty() {
	return m_front == m_rear;
}

bool CircularQueue::IsFull() {
	return (m_rear+1) % 5 == m_front;
}

int CircularQueue::Enqueue(int value) {
	if (IsFull()) {
		Warn("Queue is Full");
		return -1;
	}
	if (IsEmpty()) {
		m_front = m_rear = 0;
	}
	m_queue[m_rear] = value;
	m_rear = (m_rear + 1) % 5;
	return value;
}

int CircularQueue::Dequeue() {
	int removedValue;
	if (IsEmpty()) {
		Warn("Queue is Empty");
		return -1;
	}
	removedValue = m_queue[m_front];
	m_queue[m_front] = 0;
	m_front=(m_front +1)%5;
	return removedValue;
}

void CircularQueue::Print() {
	for (int c = 0; c <= m_rear; c++) {
		cout << "[" << c << "]" << m_queue[c] << endl;
	}
}

void CircularQueue::Warn(const char* message) {
	cout << "[WARN]" << message << endl;
}

int CircularQueue::Peek(int index) {
	return m_queue[index];
}