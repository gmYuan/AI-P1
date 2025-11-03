function deepCopy(obj, memo = new Map()) {
  // If object is null or not an object, return directly
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  // If object has already been copied, return the copy
  if (memo.has(obj)) {
    return memo.get(obj);
  }

  // Handle Date objects
  if (obj instanceof Date) {
    const copy = new Date(obj.getTime());
    memo.set(obj, copy);
    return copy;
  }

  // Handle RegExp objects
  if (obj instanceof RegExp) {
    const copy = new RegExp(obj);
    memo.set(obj, copy);
    return copy;
  }

  // Handle Array objects
  if (Array.isArray(obj)) {
    const copy = [];
    memo.set(obj, copy); // Record before recursion to handle circular references
    for (let i = 0; i < obj.length; i++) {
      copy[i] = deepCopy(obj[i], memo);
    }
    return copy;
  }

  // Handle Set objects
  if (obj instanceof Set) {
    const copy = new Set();
    memo.set(obj, copy); // Record before recursion to handle circular references
    for (const item of obj) {
      copy.add(deepCopy(item, memo));
    }
    return copy;
  }

  // Handle Map objects
  if (obj instanceof Map) {
    const copy = new Map();
    memo.set(obj, copy); // Record before recursion to handle circular references
    for (const [key, value] of obj) {
      copy.set(deepCopy(key, memo), deepCopy(value, memo));
    }
    return copy;
  }

  // Handle plain objects and class instances
  const copy = Object.create(Object.getPrototypeOf(obj));
  memo.set(obj, copy); // Record before recursion to handle circular references

  // Copy all properties including symbols
  const allKeys = [...Object.getOwnPropertyNames(obj), ...Object.getOwnPropertySymbols(obj)];
  for (const key of allKeys) {
    // Skip non-enumerable properties for simplicity, but you could include them if needed
    const descriptor = Object.getOwnPropertyDescriptor(obj, key);
    if (descriptor && (descriptor.enumerable || key === 'parent' || key === 'children')) {
      copy[key] = deepCopy(obj[key], memo);
    }
  }

  // If object has custom deepCopy method, use it
  if (typeof obj.__deepcopy__ === 'function') {
    return obj.__deepcopy__(memo);
  }

  return copy;
}

class Node {
  constructor(value) {
    this.value = value;
    this.parent = null;
    this.children = [];
  }

  addChild(child) {
    child.parent = this;
    this.children.push(child);
  }

  __deepcopy__(memo) {
    // If already in memo, return the copy
    if (memo.has(this)) {
      return memo.get(this);
    }

    // Create new instance
    const copyObj = Object.create(Object.getPrototypeOf(this));
    memo.set(this, copyObj);

    // Manually copy properties to avoid infinite recursion
    copyObj.value = deepCopy(this.value, memo);
    copyObj.parent = deepCopy(this.parent, memo);
    copyObj.children = deepCopy(this.children, memo);

    return copyObj;
  }
}

// Test code
function testDeepCopy() {
  // Test basic class deep copy
  const root = new Node("根节点");
  const child1 = new Node("子节点1");
  const child2 = new Node("子节点2");
  root.addChild(child1);
  root.addChild(child2);

  console.log("原始对象:");
  console.log(`root id: ${root}`);
  console.log(`root.children: ${root.children.map(child => child.value)}`);
  console.log(`child1.parent.value: ${child1.parent.value}`);

  console.log("\n深拷贝后:");
  const deepCopyObj = deepCopy(root);
  console.log(`deepCopy id: ${deepCopyObj}`);
  console.log(`deepCopy.children: ${deepCopyObj.children.map(child => child.value)}`);
  console.log(`deepCopy.children[0].parent.value: ${deepCopyObj.children[0].parent.value}`);

  // Verify it's actually a deep copy
  console.log(`\n验证深拷贝:`);
  console.log(`root === deepCopyObj: ${root === deepCopyObj}`);
  console.log(`root.children[0] === deepCopyObj.children[0]: ${root.children[0] === deepCopyObj.children[0]}`);
  console.log(`child1.parent === deepCopyObj.children[0].parent: ${child1.parent === deepCopyObj.children[0].parent}`);

  // Test circular references
  console.log("\n测试循环引用:");
  const nodeA = new Node("A");
  const nodeB = new Node("B");
  nodeA.addChild(nodeB);
  nodeB.addChild(nodeA); // Create circular reference

  try {
    const copied = deepCopy(nodeA);
    console.log("循环引用拷贝成功");
    console.log(`原始A的children[0].value: ${nodeA.children[0].value}`);
    console.log(`拷贝A的children[0].value: ${copied.children[0].value}`);
    console.log(`原始B的children[0].value: ${nodeB.children[0].value}`);
    console.log(`拷贝B的children[0].value: ${copied.children[0].children[0].value}`);
  } catch (e) {
    console.log(`循环引用拷贝失败: ${e}`);
  }

  // Test other data types
  console.log("\n测试其他数据类型:");

  // Test Date
  const originalDate = new Date('2023-01-01');
  const copiedDate = deepCopy(originalDate);
  console.log(`Date copied: ${originalDate.getTime() === copiedDate.getTime() && originalDate !== copiedDate}`);

  // Test Set
  const originalSet = new Set([1, 2, 3]);
  const copiedSet = deepCopy(originalSet);
  console.log(`Set copied: ${Array.from(originalSet).join(',') === Array.from(copiedSet).join(',') && originalSet !== copiedSet}`);

  // Test Map
  const originalMap = new Map([['key1', 'value1'], ['key2', 'value2']]);
  const copiedMap = deepCopy(originalMap);
  console.log(`Map copied: ${Array.from(originalMap.entries()).toString() === Array.from(copiedMap.entries()).toString() && originalMap !== copiedMap}`);
}

// Run tests
testDeepCopy();