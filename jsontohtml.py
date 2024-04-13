import sys
import os
import json

# def any_tree_to_html(node, layer):
#   results = ''

#   if 'IMAGEVIEW' in node["class"]:
#     node_type = 'img'
#   elif 'BUTTON' in node["class"]:
#     node_type = 'button'
#   elif 'EDITTEXT' in node["class"]:
#     node_type = 'input'
#   elif 'TEXTVIEW' in node["class"]:
#     node_type = 'p'
#   else:
#     node_type = 'div'
#   if node.is_leaf and node.visible:
#     html_close_tag = node_type
#     results = '<{}{}{}{}> {} </{}>\n'.format(
#         node_type,
#         ' id={}'.format(node.leaf_id) if node.leaf_id != -1 else '',
#         ' class="{}"'.format(' '.join(node.resource_id))
#         if node.resource_id
#         else '',
#         ' alt="{}"'.format(node.content_desc) if node.content_desc else '',
#         '{}, '.format(node.text) if node.text else '',
#         html_close_tag,
#     )
#   else:
#     children_results = ''
#     for child in node.children:
#       children_results += any_tree_to_html(child, layer + 1)
#       results += children_results

#   return results

def JSONtoHTML(node, layer, nextLeafId):
  results = ''

  if 'ImageView' in node["class"] or "VideoView" in node["class"]:
    node_type = 'img'
  elif 'Button' in node["class"]:
    node_type = 'button'
  elif 'EditText' in node["class"]:
    node_type = 'input'
  elif 'TextView' in node["class"]:
    node_type = 'p'
  else:
    node_type = 'div'

  isVisible = node["visibility"] == "visible"
  isLeaf = "children" not in node.keys()

  if isLeaf:
    if isVisible:
      results = '<{}{}{}{}> {} </{}>\n'.format(
        node_type,
        ' id={}'.format(leafId[0]),
        ' class={}'.format(node["resource-id"].split("/")[1]) if "resource-id" in node else "",
        ' alt="{}"'.format(node["content-desc"]) if node["content-desc"] != [None] else "",
        node["text"] if "text" in node else "",
        node_type
        )
      nextLeafId[0] += 1
  else:
    for child in node["children"]:
      results += JSONtoHTML(child, layer + 1, nextLeafId)

  return results

if __name__ == "__main__":
  directory = sys.argv[1]

  output = open(directory + "screenSummary.txt", "w")

  counter = 1
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and filename.endswith(".json"):
        output.write("Screen " + str(counter) + ":\n\n")
        counter += 1

        fileContents = open(f, "r").read()
        node = json.loads(str(fileContents))

        # Funky integet aliasing in python
        leafId = [0]
        output.write(JSONtoHTML(node["activity"]["root"], 0, leafId))
        output.write("\n\n")