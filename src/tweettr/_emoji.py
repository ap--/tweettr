"""emoji parsing for tweet texts"""
__author__ = "Andreas Poehlmann"
__email__ = "andreas@poehlmann.io"

import re

# This regex pattern matches a single emoji
# ported from: https://github.com/twitter/twitter-text
EMOJI_REGEX = re.compile(
    "[\U0001f468][\U0001f3fb-\U0001f3ff]?\u200d(?:\u2695\ufe0f|\u2696\ufe0f"
    "|\u2708\ufe0f|[\U0001f33e\U0001f373\U0001f393\U0001f3a4\U0001f3a8"
    "\U0001f3eb\U0001f3ed\U0001f4bb\U0001f4bc\U0001f527\U0001f52c"
    "\U0001f680\U0001f692\U0001f9b0-\U0001f9b3])"
    "|[\u26f9\U0001f3cb\U0001f3cc\U0001f574\U0001f575](?:[\ufe0f\U0001f3fb-\U0001f3ff]"
    "\u200d[\u2640\u2642]\ufe0f)"
    "|[\U0001f3c3\U0001f3c4\U0001f3ca\U0001f46e\U0001f471\U0001f473\U0001f477\U0001f481"
    "\U0001f482\U0001f486\U0001f487\U0001f645-\U0001f647\U0001f64b\U0001f64d\U0001f64e"
    "\U0001f6a3\U0001f6b4-\U0001f6b6\U0001f926\U0001f935\U0001f937-\U0001f939\U0001f93d"
    "\U0001f93e\U0001f9b8\U0001f9b9\U0001f9d6-\U0001f9dd][\U0001f3fb-\U0001f3ff]?"
    "\u200d[\u2640\u2642]\ufe0f"
    "|(?:\U0001f468\u200d\u2764\ufe0f\u200d\U0001f48b\u200d\U0001f468"
    "|\U0001f469\u200d\u2764\ufe0f\u200d\U0001f48b\u200d[\U0001f468\U0001f469]"
    "|\U0001f468\u200d\U0001f468\u200d\U0001f466\u200d\U0001f466"
    "|\U0001f468\u200d\U0001f468\u200d\U0001f467\u200d[\U0001f466\U0001f467]"
    "|\U0001f468\u200d\U0001f469\u200d\U0001f466\u200d\U0001f466"
    "|\U0001f468\u200d\U0001f469\u200d\U0001f467\u200d[\U0001f466\U0001f467]"
    "|\U0001f469\u200d\U0001f469\u200d\U0001f466\u200d\U0001f466"
    "|\U0001f469\u200d\U0001f469\u200d\U0001f467\u200d[\U0001f466\U0001f467]"
    "|\U0001f468\u200d\u2764\ufe0f\u200d\U0001f468"
    "|\U0001f469\u200d\u2764\ufe0f\u200d[\U0001f468\U0001f469]"
    "|\U0001f468\u200d\U0001f466\u200d\U0001f466"
    "|\U0001f468\u200d\U0001f467\u200d[\U0001f466\U0001f467]"
    "|\U0001f468\u200d\U0001f468\u200d[\U0001f466\U0001f467]"
    "|\U0001f468\u200d\U0001f469\u200d[\U0001f466\U0001f467]"
    "|\U0001f469\u200d\U0001f466\u200d\U0001f466"
    "|\U0001f469\u200d\U0001f467\u200d[\U0001f466\U0001f467]"
    "|\U0001f469\u200d\U0001f469\u200d[\U0001f466\U0001f467]"
    "|\U0001f3f3\ufe0f\u200d\U0001f308"
    "|\U0001f3f4\u200d\u2620\ufe0f"
    "|\U0001f46f\u200d\u2640\ufe0f"
    "|\U0001f46f\u200d\u2642\ufe0f"
    "|\U0001f93c\u200d\u2640\ufe0f"
    "|\U0001f93c\u200d\u2642\ufe0f"
    "|\U0001f9de\u200d\u2640\ufe0f"
    "|\U0001f9de\u200d\u2642\ufe0f"
    "|\U0001f9df\u200d\u2640\ufe0f"
    "|\U0001f9df\u200d\u2642\ufe0f"
    "|\U0001f441\u200d\U0001f5e8"
    "|\U0001f468\u200d[\U0001f466\U0001f467]"
    "|\U0001f469\u200d[\U0001f466\U0001f467])"
    "|[#*0-9]\ufe0f?\u20e3"
    "|(?:[©®\u2122\u265f]\ufe0f)"
    "|[\u203c\u2049\u2139\u2194-\u2199\u21a9\u21aa\u231a\u231b\u2328\u23cf\u23ed-\u23ef"
    "\u23f1\u23f2\u23f8-\u23fa\u24c2\u25aa\u25ab\u25b6\u25c0\u25fb-\u25fe\u2600-\u2604"
    "\u260e\u2611\u2614\u2615\u2618\u2620\u2622\u2623\u2626\u262a\u262e\u262f\u2638-\u263a"
    "\u2640\u2642\u2648-\u2653\u2660\u2663\u2665\u2666\u2668\u267b\u267f\u2692-\u2697\u2699"
    "\u269b\u269c\u26a0\u26a1\u26aa\u26ab\u26b0\u26b1\u26bd\u26be\u26c4\u26c5\u26c8\u26cf"
    "\u26d1\u26d3\u26d4\u26e9\u26ea\u26f0-\u26f5\u26f8\u26fa\u26fd\u2702\u2708\u2709\u270f"
    "\u2712\u2714\u2716\u271d\u2721\u2733\u2734\u2744\u2747\u2757\u2763\u2764\u27a1\u2934"
    "\u2935\u2b05-\u2b07\u2b1b\u2b1c\u2b50\u2b55\u3030\u303d\u3297\u3299\U0001f004\U0001f170"
    "\U0001f171\U0001f17e\U0001f17f\U0001f202\U0001f21a\U0001f22f\U0001f237\U0001f321"
    "\U0001f324-\U0001f32c\U0001f336\U0001f37d\U0001f396\U0001f397\U0001f399-\U0001f39b"
    "\U0001f39e\U0001f39f\U0001f3cd\U0001f3ce\U0001f3d4-\U0001f3df\U0001f3f3\U0001f3f5"
    "\U0001f3f7\U0001f43f\U0001f441\U0001f4fd\U0001f549\U0001f54a\U0001f56f\U0001f570"
    "\U0001f573\U0001f576-\U0001f579\U0001f587\U0001f58a-\U0001f58d\U0001f5a5\U0001f5a8"
    "\U0001f5b1\U0001f5b2\U0001f5bc\U0001f5c2-\U0001f5c4\U0001f5d1-\U0001f5d3"
    "\U0001f5dc-\U0001f5de\U0001f5e1\U0001f5e3\U0001f5e8\U0001f5ef\U0001f5f3\U0001f5fa"
    "\U0001f6cb\U0001f6cd-\U0001f6cf\U0001f6e0-\U0001f6e5\U0001f6e9\U0001f6f0\U0001f6f3]"
    "(?:\ufe0f|(?!\ufe0e))"
    "|(?:[\u261d\u26f7\u26f9\u270c\u270d\U0001f3cb\U0001f3cc\U0001f574\U0001f575\U0001f590]"
    "(?:\ufe0f|(?!\ufe0e))"
    "|[\u270a\u270b\U0001f385\U0001f3c2-\U0001f3c4\U0001f3c7\U0001f3ca\U0001f442\U0001f443"
    "\U0001f446-\U0001f450\U0001f466-\U0001f469\U0001f46e\U0001f470-\U0001f478\U0001f47c"
    "\U0001f481-\U0001f483\U0001f485-\U0001f487\U0001f4aa\U0001f57a\U0001f595\U0001f596"
    "\U0001f645-\U0001f647\U0001f64b-\U0001f64f\U0001f6a3\U0001f6b4-\U0001f6b6\U0001f6c0"
    "\U0001f6cc\U0001f918-\U0001f91c\U0001f91e\U0001f91f\U0001f926\U0001f930-\U0001f939"
    "\U0001f93d\U0001f93e\U0001f9b5\U0001f9b6\U0001f9b8\U0001f9b9\U0001f9d1-\U0001f9dd])"
    "[\U0001f3fb-\U0001f3ff]?"
    "|(?:\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f"
    "|\U0001f3f4\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f"
    "|\U0001f3f4\U000e0067\U000e0062\U000e0077\U000e006c\U000e0073\U000e007f"
    "|\U0001f1e6[\U0001f1e8-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f2"
    "\U0001f1f4\U0001f1f6-\U0001f1fa\U0001f1fc\U0001f1fd\U0001f1ff]"
    "|\U0001f1e7[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ef\U0001f1f1-\U0001f1f4"
    "\U0001f1f6-\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1fe\U0001f1ff]"
    "|\U0001f1e8[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ee\U0001f1f0-\U0001f1f5"
    "\U0001f1f7\U0001f1fa-\U0001f1ff]"
    "|\U0001f1e9[\U0001f1ea\U0001f1ec\U0001f1ef\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1ff]"
    "|\U0001f1ea[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ed\U0001f1f7-\U0001f1fa]"
    "|\U0001f1eb[\U0001f1ee-\U0001f1f0\U0001f1f2\U0001f1f4\U0001f1f7]"
    "|\U0001f1ec[\U0001f1e6\U0001f1e7\U0001f1e9-\U0001f1ee\U0001f1f1-\U0001f1f3"
    "\U0001f1f5-\U0001f1fa\U0001f1fc\U0001f1fe]"
    "|\U0001f1ed[\U0001f1f0\U0001f1f2\U0001f1f3\U0001f1f7\U0001f1f9\U0001f1fa]"
    "|\U0001f1ee[\U0001f1e8-\U0001f1ea\U0001f1f1-\U0001f1f4\U0001f1f6-\U0001f1f9]"
    "|\U0001f1ef[\U0001f1ea\U0001f1f2\U0001f1f4\U0001f1f5]"
    "|\U0001f1f0[\U0001f1ea\U0001f1ec-\U0001f1ee\U0001f1f2\U0001f1f3\U0001f1f5\U0001f1f7"
    "\U0001f1fc\U0001f1fe\U0001f1ff]"
    "|\U0001f1f1[\U0001f1e6-\U0001f1e8\U0001f1ee\U0001f1f0\U0001f1f7-\U0001f1fb\U0001f1fe]"
    "|\U0001f1f2[\U0001f1e6\U0001f1e8-\U0001f1ed\U0001f1f0-\U0001f1ff]"
    "|\U0001f1f3[\U0001f1e6\U0001f1e8\U0001f1ea-\U0001f1ec\U0001f1ee\U0001f1f1\U0001f1f4"
    "\U0001f1f5\U0001f1f7\U0001f1fa\U0001f1ff]"
    "|\U0001f1f4\U0001f1f2"
    "|\U0001f1f5[\U0001f1e6\U0001f1ea-\U0001f1ed\U0001f1f0-\U0001f1f3"
    "\U0001f1f7-\U0001f1f9\U0001f1fc\U0001f1fe]"
    "|\U0001f1f6\U0001f1e6"
    "|\U0001f1f7[\U0001f1ea\U0001f1f4\U0001f1f8\U0001f1fa\U0001f1fc]"
    "|\U0001f1f8[\U0001f1e6-\U0001f1ea\U0001f1ec-\U0001f1f4\U0001f1f7-\U0001f1f9\U0001f1fb\U0001f1fd-\U0001f1ff]"
    "|\U0001f1f9[\U0001f1e6\U0001f1e8\U0001f1e9\U0001f1eb-\U0001f1ed\U0001f1ef-\U0001f1f4"
    "\U0001f1f7\U0001f1f9\U0001f1fb\U0001f1fc\U0001f1ff]"
    "|\U0001f1fa[\U0001f1e6\U0001f1ec\U0001f1f2\U0001f1f3\U0001f1f8\U0001f1fe\U0001f1ff]"
    "|\U0001f1fb[\U0001f1e6\U0001f1e8\U0001f1ea\U0001f1ec\U0001f1ee\U0001f1f3\U0001f1fa]"
    "|\U0001f1fc[\U0001f1eb\U0001f1f8]"
    "|\U0001f1fd\U0001f1f0"
    "|\U0001f1fe[\U0001f1ea\U0001f1f9]"
    "|\U0001f1ff[\U0001f1e6\U0001f1f2\U0001f1fc]"
    "|[\u23e9-\u23ec\u23f0\u23f3\u267e\u26ce\u2705\u2728\u274c\u274e\u2753-\u2755\u2795-\u2797"
    "\u27b0\u27bf\ue50a\U0001f0cf\U0001f18e\U0001f191-\U0001f19a\U0001f1e6-\U0001f1ff\U0001f201"
    "\U0001f232-\U0001f236\U0001f238-\U0001f23a\U0001f250\U0001f251\U0001f300-\U0001f320"
    "\U0001f32d-\U0001f335\U0001f337-\U0001f37c\U0001f37e-\U0001f384\U0001f386-\U0001f393"
    "\U0001f3a0-\U0001f3c1\U0001f3c5\U0001f3c6\U0001f3c8\U0001f3c9\U0001f3cf-\U0001f3d3"
    "\U0001f3e0-\U0001f3f0\U0001f3f4\U0001f3f8-\U0001f43e\U0001f440\U0001f444\U0001f445"
    "\U0001f451-\U0001f465\U0001f46a-\U0001f46d\U0001f46f\U0001f479-\U0001f47b"
    "\U0001f47d-\U0001f480\U0001f484\U0001f488-\U0001f4a9\U0001f4ab-\U0001f4fc"
    "\U0001f4ff-\U0001f53d\U0001f54b-\U0001f54e\U0001f550-\U0001f567\U0001f5a4\U0001f5fb-\U0001f644"
    "\U0001f648-\U0001f64a\U0001f680-\U0001f6a2\U0001f6a4-\U0001f6b3\U0001f6b7-\U0001f6bf\U0001f6c1-\U0001f6c5"
    "\U0001f6d0-\U0001f6d2\U0001f6eb\U0001f6ec\U0001f6f4-\U0001f6f9\U0001f910-\U0001f917\U0001f91d"
    "\U0001f920-\U0001f925\U0001f927-\U0001f92f\U0001f93a\U0001f93c\U0001f940-\U0001f945\U0001f947-\U0001f970"
    "\U0001f973-\U0001f976\U0001f97a\U0001f97c-\U0001f9a2\U0001f9b4\U0001f9b7\U0001f9c0-\U0001f9c2\U0001f9d0"
    "\U0001f9de-\U0001f9ff])"
    "|\ufe0f"
)


def iter_emoji_entities(text):
    """iterates all emojis in a text"""
    for match in EMOJI_REGEX.finditer(text):
        yield {
            'text': match.group(0),
            'indices': match.span(0),
        }
