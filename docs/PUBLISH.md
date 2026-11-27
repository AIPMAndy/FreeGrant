# GitHub 开源发布与维护

1. 仓库 Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save。
2. 部署完成后以 GitHub 显示的真实站点地址为准，打开首页检查政策筛选、CSV导出、打印保存PDF、外链与隐私。
3. 直接打开 index.html 或运行 python3 -m http.server 8000，无需API key。
4. 运行 python tests/validate.py 校验政策ID、JSON、CSV、README及网页。更新政策时同步所有格式，按 CONTRIBUTING.md 提供官方来源和核验日。
5. 原始离线PDF另行同步；网页已支持打印/保存PDF。若获得原始文件，可将 FreeGrant-Guide.pdf 放在根目录并更新下载链接。
6. 不上传个人真实资料，不假设政策一定可申报。
