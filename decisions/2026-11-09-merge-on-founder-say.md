# Merging on the founder's say-so

Made Nov 5, 2026, in the planning Project. Recorded Nov 9.

| Decision | Reason |
| --- | --- |
| When the founder tells an agent in chat to merge a specific PR, that counts as his approval. The agent merges it and notes "Merged on the founder's instruction in chat, <date>" in the PR | The founder directs the work. Making him click merge on something he already approved adds friction without adding control |
| The exception: changes to permission files, workflow `permissions:` blocks or token scopes. The founder merges those himself | An agent should never be the one to widen its own access |
