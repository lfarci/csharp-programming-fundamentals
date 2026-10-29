// Tiny inline Markdown for short texts from course.json: `code` only, everything else escaped.
export const inline = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/`([^`]+)`/g, '<code>$1</code>')
