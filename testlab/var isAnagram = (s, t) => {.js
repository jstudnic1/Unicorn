var isAnagram = (s, t) => {
    const isEqual = s.length === t.length;
    if (!isEqual) return false;

    return reorder(t) === reorder(s);
};

const reorder = (str) => str
    .split('')
    .sort((a, b) => a.localeCompare(b))
    .join('');

const f = isAnagram("anagram", "nagaram");
console.log(f)