class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class TreeNode:
            def __init__(self):
                self.children = {}
                self.deleted = False
        
        root = TreeNode()
        
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TreeNode()
                node = node.children[folder]
        
        def getStructure(node):
            if not node.children:
                return ""
            
            items = []
            for name in sorted(node.children.keys()):
                child_structure = getStructure(node.children[name])
                items.append(f"({name}{child_structure})")
            
            return "".join(items)
        
        structure_map = {}
        
        def collectStructures(node):
            structure = getStructure(node)
            if structure and structure != "":
                if structure not in structure_map:
                    structure_map[structure] = []
                structure_map[structure].append(node)
            
            for child in node.children.values():
                collectStructures(child)
        
        collectStructures(root)
        
        for nodes in structure_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True
        
        result = []
        
        def dfs(node, path):
            if node.deleted:
                return
            
            if path:
                result.append(path[:])
            
            for name, child in node.children.items():
                if not child.deleted:
                    path.append(name)
                    dfs(child, path)
                    path.pop()
        
        for name, child in root.children.items():
            if not child.deleted:
                dfs(child, [name])
        
        return result
