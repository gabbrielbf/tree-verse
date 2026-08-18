from menu import traversals
import time, sys

class Visualizer:

    def __init__(self, bst):
        self.bst = bst
    
    def _write(self, text, delay=0.04):
        """ Writes node by node dynamically """

        for char in str(text):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

    def _get_levels(self):
        """ Organizes the tree nodes by level """

        if self.bst.root is None:
            return []

        levels = [[(self.bst.root, 0)]]
        current = levels[0]

        while current:

            next_level = []

            for node, position in current:
                if node.left:
                    next_level.append((node.left, position * 2))

                if node.right:
                    next_level.append((node.right, position * 2 + 1))

            if not next_level:
                break

            levels.append(next_level)
            current = next_level

        return levels

    def _get_position(self, position, level, height, spacing):
        """ Calculates the horizontal position of a node """

        slots = 2 ** level
        distance = spacing * (2 ** (height - level - 1))

        return ((position * distance) + distance) // 2

    def display_tree(self):
        """ Displays the tree in a hierarchical format """

        if self.bst.root is None:
            self._write('[Empty tree]\n')
            return

        levels = self._get_levels()
        height = len(levels)

        # Espaço mínimo entre dois nós.
        largest_value = max(
            len(str(node.data))
            for level in levels
            for node, _ in level
        )

        spacing = max(6, largest_value + 4)
        width = (2 ** height) * spacing

        # Lógica para os nós
        for level_index, level in enumerate(levels):

            line = [' '] * width

            for node, position in level:

                x = self._get_position(
                    position,
                    level_index,
                    height,
                    spacing
                )

            value = str(node.data)

            start = x - len(value) // 2

            for index, char in enumerate(value):
                if 0 <= start + index < width:
                    line[start + index] = char

            self._write(''.join(line).rstrip() + '\n')

            # Lógica para a conexão entre os nós
            if level_index == height - 1:
                continue

            next_level = levels[level_index + 1]
            connections = [' '] * width

            for node, position in level:

                parent_x = self._get_position(
                    position,
                    level_index,
                    height,
                    spacing
                )

                if node.left:
                    child_x = self._get_position(
                        position * 2,
                        level_index + 1,
                        height,
                        spacing
                    )

                    x = (parent_x + child_x) // 2

                    if 0 <= x < width:
                        connections[x] = '/'

                if node.right:
                    child_x = self._get_position(
                        position * 2 + 1,
                        level_index + 1,
                        height,
                        spacing
                    )

                    x = (parent_x + child_x) // 2

                    if 0 <= x < width:
                        connections[x] = '\\'

            self._write(''.join(connections).rstrip() + '\n')

    # Percusos abaixo vão usar da lógica desenvolvida pelo método "display_tree" acima e elaborar suas próprias exibições de acordo
    # com a sua respeciva característica de exibição
    def _symmetric(self, node):
        if node:
            yield from self._symmetric(node.left)
            yield node.data
            yield from self._symmetric(node.right)

    def _preorder(self, node):
        if node:
            yield node.data
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.data

    def _levelorder(self):
        if self.bst.root is None:
            return

        queue = [self.bst.root]

        while queue:
            node = queue.pop(0)

            yield node.data

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)



def wich_traversal(bst):

    visualizer = Visualizer(bst)

    match traversals():
        case 1:
            pass

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

