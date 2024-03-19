# Array

```java
public void ensureCapacity(int minCapacity) {
    var current = this.array.length;
    if (minCapacity > current) {
        var new_array = new Object[Math.min(current * 2, minCapacity)];
        System.copyarray(this.array, 0, new_array, 0, size);
        this.array = new_array;
        this.index++;
    }
}
```

## Typical Problems
 