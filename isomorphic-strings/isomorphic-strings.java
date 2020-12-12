class Solution {
    public boolean isIsomorphic(String s, String t) {
//         if(s.length() > t.length() || t.length() > s.length())
//             return false;
//         Map<Character, Integer> m1 = new HashMap<>();
//         Map<Character, Integer> m2 = new HashMap<>();
//         for(int i = 0; i < s.length(); i++)
//             m1.put(s.charAt(i), m1.getOrDefault(s.charAt(i),0)+1);
        
//         for(int i = 0; i < t.length(); i++)
//             m2.put(t.charAt(i), m2.getOrDefault(t.charAt(i),0)+1);
        
//         if(m1.size() == m2.size())
//             return true;
//         else
//             return false;
                Map m = new HashMap();
    for (Integer i=0; i<s.length(); ++i)
        if (m.put(s.charAt(i), i) != m.put(t.charAt(i)+"", i))
            return false;
    return true;
    }
}
