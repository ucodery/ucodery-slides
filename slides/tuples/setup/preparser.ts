import { definePreparserSetup } from "@slidev/types";

const deck = require("../package.json");

export default definePreparserSetup(() => {
  return [
    {
      async transformSlide(content, frontmatter) {
        if (!("ribbon" in frontmatter) || frontmatter.ribbon) {
          return [
            content,
            "",
            '<div class="left-ribbon">',
            `${deck.homepage}`,
            "</div>",
            '<div class="right-ribbon">',
            "<carbon:logo-github />",
            '<span class="right-ribbon">@ucodery</span>',
            "<carbon:logo-mastodon />",
            '<span class="right-ribbon">@ucodery@fosstodon.org</span>',
            "</div>",
          ].join("\n");
        }
      },
    },
  ];
});
