class DynamicArray {
  int cap;
  int size = 0;
  int *backing;

public:
  DynamicArray(int capacity) { 
    cap = capacity; 
    backing = new int[cap];
  }

  int get(int i) {
    return backing[i];
  }

  void set(int i, int n) {
    backing[i] = n;
  }

  void pushback(int n) {
    if (size >= cap) {
      resize();
    }

    set(size, n);
    size++;
  }

  int popback() {
    size -= 1;
    return backing[size];
  }

  void resize() {
    int *doubled = new int[2 * cap];
    for (int i = 0; i < size; i++) {
      doubled[i] = backing[i];
    }

    delete backing;
    backing = doubled;
    cap *= 2;
  }

  int getSize() {
    return size;
  }

  int getCapacity() {
    return cap;
  }
};
