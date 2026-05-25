import os
import re
import datetime
import random
import json

# 定义博客文章目录和模板文件路径
BLOG_DIR = "d:\\小程序\\web-tools_aichatx.com.cn\\blog"
TEMPLATE_FILE = "d:\\小程序\\web-tools_aichatx.com.cn\\blog_template.html"
INDEX_FILE = "d:\\小程序\\web-tools_aichatx.com.cn\\blog\\index.html"
GENERATED_BLOGS_JSON = "d:\\小程序\\web-tools_aichatx.com.cn\\generated_blogs.json"

def load_generated_blogs():
    if os.path.exists(GENERATED_BLOGS_JSON):
        with open(GENERATED_BLOGS_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_generated_blogs(blogs):
    with open(GENERATED_BLOGS_JSON, "w", encoding="utf-8") as f:
        json.dump(blogs, f, ensure_ascii=False, indent=4)

# 博客文章数据结构
blog_posts_data = [
    {
        "title": "利用AI工具提升个人效率：从信息过载到精准决策",
        "description": "探讨如何在日常工作和学习中，有效利用各类AI工具，处理信息、辅助决策、自动化重复任务，从而真正提升个人效率和产出。",
        "category": "效率提升",
        "read_time": 10,
        "content": """
            <p>在当今信息爆炸的时代，我们每天都被海量的数据和各种通知所淹没。如何从这股洪流中脱身，不仅不被信息所累，反而能借力实现效率飞跃，是每个现代人都面临的挑战。而人工智能，正是我们手中的那把“破局之剑”。</p>

            <h2>一、告别“大海捞针”：AI 辅助信息处理</h2>
            <p>传统的信息检索和筛选耗时耗力。AI工具的出现，彻底改变了这一局面。无论是阅读一篇冗长的报告，还是浏览无数的新闻动态，AI都能迅速提炼核心要点。</p>
            <ul>
                <li><strong>智能摘要：</strong> 利用AI工具，一键生成文章、文档的精炼摘要，快速掌握核心内容，节省大量阅读时间。</li>
                <li><strong>多语言翻译与理解：</strong> 借助AI翻译工具，轻松跨越语言障碍，获取全球前沿资讯。更重要的是，AI还能辅助理解特定领域的术语和语境。</li>
                <li><strong>知识库构建：</strong> 将碎片化信息通过AI整理、归纳，形成结构化的个人知识库，方便随时检索和学习。</li>
            </ul>

            <h2>二、从“凭感觉”到“数据驱动”：AI 辅助精准决策</h2>
            <p>面对复杂问题，人类的决策往往受限于经验和认知偏差。AI能够基于大数据和复杂算法，提供更客观、全面的分析视角。</p>
            <ul>
                <li><strong>数据分析与可视化：</strong> AI工具能够处理庞大的数据集，识别模式、趋势和异常，并将结果以直观的图表展示，帮助我们洞察数据背后的含义。</li>
                <li><strong>方案模拟与预测：</strong> 在商业决策、项目规划等领域，AI可以模拟不同方案的潜在结果，预测风险和收益，从而支持我们做出更明智的选择。</li>
                <li><strong>个性化推荐：</strong> 基于个人偏好和行为数据，AI能推荐最符合我们需求的信息、工具或解决方案，减少选择焦虑。</li>
            </ul>

            <h2>三、释放双手：AI 自动化重复任务</h2>
            <p>许多日常工作都包含大量重复性、规则性的任务，这些是AI自动化的绝佳目标。</p>
            <ul>
                <li><strong>智能日程管理：</strong> AI日历能根据你的工作习惯和优先级，自动安排会议、提醒任务，甚至优化出行路线。</li>
                <li><strong>邮件与文档自动化：</strong> AI可以辅助分类邮件、草拟回复，甚至自动生成会议纪要或报告初稿，让你将精力集中于更高价值的创造性工作。</li>
                <li><strong>内容生成辅助：</strong> 对于需要大量文案的场景（如营销、社交媒体），AI能在你提供少量关键信息后，快速生成多种风格的初稿，大大提高效率。</li>
            </ul>

            <h2>四、AI 是工具，而非替代：构建人类与AI的协作模式</h2>
            <p>值得强调的是，AI的价值在于“辅助”和“增强”，而非“替代”。过度依赖AI，放弃独立思考，反而会让我们失去核心竞争力。</p>
            <div class="quote">
                “最好的AI用户，是那些能够熟练驾驭AI，并将其融入自身工作流，同时保持批判性思维和人类独特创造力的人。”
            </div>
            <p>我们需要学会提出好的问题、审视AI的输出、结合自身经验进行判断和优化。将AI视为一位高效的“副驾驶”，在它的辅助下，我们能够看得更远、走得更快。</p>

            <h2>五、总结：迈向AI赋能的“超个体”</h2>
            <p>AI工具正在重塑我们的工作和生活方式。学会驾驭这些工具，不仅能帮助我们摆脱信息过载的困境，更能让我们成为一个具备更强信息处理能力、决策能力和创新能力的“超个体”。与其焦虑于AI的冲击，不如主动拥抱它，让它成为我们提升效率、实现价值的强大盟友。</p>
        """
    },
    {
        "title": "前端开发者必备的5个效率工具：告别重复劳动，聚焦核心创造",
        "description": "针对前端开发者，介绍除了常见的代码编辑器和版本控制工具之外，能够显著提升开发效率、优化工作流程的5个实用工具或技术。",
        "category": "开发效率",
        "read_time": 8,
        "content": """
            <p>前端开发的世界日新月异，工具层出不穷。作为一名开发者，我们常常在追赶新技术的浪潮中感到疲惫。然而，真正的效率提升并非在于掌握所有最新技术，而在于选择那些能真正解放生产力、让你的代码更健壮、工作流更顺畅的“神兵利器”。本文将为你揭秘五款前端开发者必备的效率工具，助你告别重复劳动，将宝贵精力聚焦于核心创造。</p>

            <h2>一、CSS 预处理器/后处理器：告别手写重复样式</h2>
            <p>Sass、Less、Stylus等预处理器，以及PostCSS这样的后处理器，早已成为现代前端开发的标配。它们通过变量、混合（Mixin）、函数、嵌套等高级特性，让CSS编写变得更具逻辑性、可维护性。</p>
            <ul>
                <li><strong>Sass/Less：</strong> 允许你定义颜色、字体等变量，避免魔法字符串；通过Mixin复用常用样式块；嵌套规则让CSS结构与HTML结构保持一致，提高可读性。</li>
                <li><strong>PostCSS：</strong> 则更像是一个CSS的“瑞士军刀”，通过插件机制实现自动添加厂商前缀、CSS模块化、CSS变量转换等功能，让你的CSS兼容性更强，体积更小。</li>
            </ul>
            <p>告别繁琐的手动调整，让这些工具帮你自动化处理CSS的重复性工作。</p>

            <h2>二、组件库与设计系统：加速UI构建与保持一致性</h2>
            <p>无论是React、Vue还是Angular，组件化开发已经是主流。一个高质量的组件库或内部设计系统，能极大提升开发效率，同时确保产品UI的一致性。</p>
            <ul>
                <li><strong>成熟组件库：</strong> 如Ant Design、Element UI、Material-UI等，提供了开箱即用的高质量UI组件，涵盖了大部分常见的交互场景。它们不仅美观，而且经过了大量实践验证，稳定可靠。</li>
                <li><strong>内部设计系统：</strong> 对于大型项目或团队，建立自己的设计系统是更优解。它包含了一套共享的设计原则、UI规范和可复用组件，让不同开发者、设计师之间高效协作，保证产品视觉和交互的统一。</li>
            </ul>
            <p>将精力从繁琐的UI实现中解放出来，聚焦于业务逻辑的实现。</p>

            <h2>三、自动化测试框架：代码质量的“守护神”</h2>
            <p>在快节奏的开发中，测试常常被忽视。但没有测试的代码，就像在薄冰上跳舞。自动化测试框架（如Jest、React Testing Library、Cypress、Playwright）是保障代码质量、减少Bug、提高项目可维护性的关键。</p>
            <ul>
                <li><strong>单元测试（Jest）：</strong> 针对函数、组件等最小单位进行测试，确保每个模块的行为符合预期。</li>
                <li><strong>集成测试（React Testing Library）：</strong> 模拟用户行为，测试多个模块协同工作时的表现。</li>
                <li><strong>端到端测试（Cypress/Playwright）：</strong> 模拟真实用户在浏览器中的完整操作路径，确保整个应用流程的正确性。</li>
            </ul>
            <p>虽然编写测试用例需要投入时间，但长期来看，它能为你节省无数调试Bug的痛苦时间。</p>

            <h2>四、现代化构建工具（Vite/Webpack）：优化开发体验与项目性能</h2>
            <p>项目的构建速度和最终产物性能，直接影响开发体验和用户体验。Webpack曾是构建工具的霸主，但Vite等新一代工具的崛起，带来了更快的开发服务器启动速度和热模块更新（HMR）。</p>
            <ul>
                <li><strong>Vite：</strong> 利用ES模块的原生支持，实现按需编译，开发服务器启动速度快如闪电；Rollup作为生产环境打包器，打包效率也极高。</li>
                <li><strong>Webpack：</strong> 依然是功能最强大的构建工具，生态庞大，配置灵活，适合大型复杂项目。通过合理的配置优化，也能达到很好的性能表现。</li>
            </ul>
            <p>选择合适的构建工具，能让你的开发流程如丝般顺滑，同时为用户提供更快的加载体验。</p>

            <h2>五、浏览器开发者工具高级技巧：深入调试与性能分析</h2>
            <p>浏览器开发者工具是前端开发者最亲密的伙伴，但很多人只停留在Element和Console面板。深入挖掘其高级功能，能让你成为一个更高效的调试高手。</p>
            <ul>
                <li><strong>Performance面板：</strong> 分析页面加载、渲染、脚本执行等性能瓶颈，找出优化点。</li>
                <li><strong>Network面板：</strong> 监控网络请求，分析资源加载瀑布流，发现潜在的网络问题。</li>
                <li><strong>Sources面板：</strong> 断点调试、代码步进、修改运行时代码，快速定位和修复Bug。</li>
                <li><strong>Memory面板：</strong> 检测内存泄漏，优化应用的内存占用。</li>
            </ul>
            <p>熟练掌握开发者工具的高级用法，就像拥有了一双透视眼，能让你更深入地理解应用的运行机制。</p>

            <h2>总结：持续学习，选择最适合你的“组合拳”</h2>
            <p>以上五类工具只是冰山一角，前端技术的海洋广阔无垠。没有最好的工具，只有最适合你的工具。关键在于持续学习，勇于尝试，并根据项目需求和团队实际情况，组合出最能提升效率的“组合拳”。让工具成为你的翅膀，而非束缚，去创造更精彩的用户体验吧！</p>
        """
    },
    {
        "title": "深度解析：现代网络应用中的数据安全与隐私保护实践",
        "description": "从用户的角度出发，深入浅出地讲解现代网络应用中数据安全与隐私保护的重要性，以及开发者在构建应用时应遵循的最佳实践，让用户了解自己的数据如何被保护。",
        "category": "安全指南",
        "read_time": 12,
        "content": """
            <p>在这个数字化高度发达的时代，我们的生活几乎与网络应用密不可分。从社交媒体到在线购物，从移动支付到远程办公，我们享受着技术带来的便利，但同时也面临着一个日益严峻的挑战——数据安全与隐私保护。每一次数据泄露事件，都敲响了警钟：我们的个人信息，真的安全吗？本文将从开发者和用户的双重视角，深度解析现代网络应用中的数据安全与隐私保护实践。</p>

            <h2>一、为什么数据安全与隐私保护如此重要？</h2>
            <p>数据，被称为新时代的“石油”。它不仅是企业决策、产品优化的核心资产，更是个人身份的映射。一旦数据泄露，后果不堪设想：</p>
            <ul>
                <li><strong>个人信息：</strong> 身份证号、电话、住址、健康状况等敏感信息被滥用，可能导致电信诈骗、精准骚扰甚至身份盗用。</li>
                <li><strong>财务数据：</strong> 银行卡号、支付密码泄露，直接威胁财产安全。</li>
                <li><strong>商业机密：</strong> 企业数据外泄，可能导致巨大的经济损失和竞争劣势。</li>
                <li><strong>声誉受损：</strong> 无论是个人还是企业，数据安全事件都会严重损害信任和品牌形象。</li>
            </ul>
            <p>因此，数据安全与隐私保护不仅仅是技术问题，更是道德底线和社会责任。</p>

            <h2>二、开发者如何构建坚不可摧的数据防线？</h2>
            <p>作为网络应用的构建者，开发者肩负着保护用户数据的重任。以下是一些关键的实践原则：</p>
            <h3>1. 传输加密：HTTPS 是基石</h3>
            <p>确保所有数据在用户浏览器和服务器之间传输时都经过加密。HTTPS（HTTP Secure）是强制性的，它通过SSL/TLS协议对通信内容进行加密，防止数据在传输过程中被窃听或篡改。</p>
            <h3>2. 数据存储安全：多层防护</h3>
            <p>数据存储在服务器端时，同样需要严密保护。</p>
            <ul>
                <li><strong>数据库加密：</strong> 敏感数据在数据库中应加密存储，即使数据库被攻破，攻击者也难以直接获取明文信息。</li>
                <li><strong>访问控制：</strong> 实施严格的权限管理，只有授权的用户和系统才能访问特定的数据。</li>
                <li><strong>定期备份与恢复：</strong> 建立完善的备份策略，以应对数据损坏或丢失的情况。</li>
            </ul>
            <h3>3. 身份认证与授权：守护用户入口</h3>
            <p>用户的身份验证是访问控制的第一道门槛。</p>
            <ul>
                <li><strong>强密码策略：</strong> 强制用户使用复杂密码，并定期提醒更换。</li>
                <li><strong>多因素认证（MFA）：</strong> 额外增加一道安全验证（如手机验证码、指纹），即使密码泄露也能有效防护。</li>
                <li><strong>OAuth/OpenID Connect：</strong> 对于第三方登录，采用标准的授权协议，避免直接处理用户凭证。</li>
            </ul>
            <h3>4. 最小权限原则：按需访问</h3>
            <p>无论是系统组件还是开发人员，都应遵循“最小权限原则”，即只授予完成其任务所需的最小权限。这能有效限制潜在攻击的范围和影响。</p>
            <h3>5. 安全审计与漏洞扫描：防患于未然</h3>
            <p>安全是一个持续的过程，而非一劳永逸。开发者需要：</p>
            <ul>
                <li><strong>定期进行安全审计：</strong> 检查代码、系统配置和操作流程是否存在安全隐患。</li>
                <li><strong>利用自动化漏洞扫描工具：</strong> 及时发现并修复已知的安全漏洞。</li>
                <li><strong>关注安全社区动态：</strong> 及时了解最新的攻击手段和防护措施。</li>
            </ul>

            <h2>三、用户如何保护自己的数据？</h2>
            <p>数据安全并非开发者单方面的责任，用户也扮演着重要角色。</p>
            <ul>
                <li><strong>使用强密码并定期更换：</strong> 避免使用弱密码和在多个网站重复使用密码。</li>
                <li><strong>开启多因素认证：</strong> 尽可能为重要账户开启MFA。</li>
                <li><strong>警惕钓鱼诈骗：</strong> 不随意点击不明链接，不泄露个人敏感信息。</li>
                <li><strong>阅读隐私政策：</strong> 了解应用如何收集、使用和分享你的数据。</li>
                <li><strong>及时更新软件：</strong> 软件更新通常包含安全补丁，能修复已知漏洞。</li>
            </ul>

            <h2>四、总结：安全与隐私，共建信任的数字世界</h2>
            <p>在构建现代网络应用时，数据安全与隐私保护是不可或缺的核心要素。开发者必须将其融入产品设计的每一个环节，从技术到管理，建立全方位的防护体系。同时，用户也应提高安全意识，成为自身数据的第一道防线。只有开发者与用户共同努力，才能在享受数字化便利的同时，共建一个安全、可信赖的数字世界。</p>
        """
    }
]

def generate_slug(title):
    # 尝试从标题中提取英文单词和数字
    english_words_and_numbers = re.findall(r'[a-zA-Z0-9]+', title)
    
    if english_words_and_numbers:
        # 如果找到英文单词或数字，用它们构建slug
        slug = '-'.join(english_words_and_numbers).lower()
    else:
        # 如果标题中没有英文单词或数字（即纯中文），则生成一个基于时间的通用slug
        # 这确保了slug是ASCII且唯一，但缺乏语义。
        now = datetime.datetime.now()
        slug = f"blog-post-{now.strftime('%Y%m%d%H%M%S')}"
    
    # 清理slug，确保没有连续的连字符或首尾连字符
    slug = re.sub(r'-+', '-', slug).strip('-')
    
    return slug

def create_blog_post(post_data):
    title = post_data["title"]
    description = post_data["description"]
    category = post_data["category"]
    read_time = post_data["read_time"]
    content = post_data["content"]

    slug = generate_slug(title)
    filename = f"{slug}.html"
    filepath = os.path.join(BLOG_DIR, filename)

    # 检查文章是否已存在，如果存在则跳过
    if os.path.exists(filepath):
        print(f"文章 '{title}' (文件: {filename}) 已存在，跳过生成。")
        return None

    # 读取模板内容
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    # 替换模板中的占位符
    today = datetime.date.today().strftime("%Y-%m-%d")
    canonical_url = f"https://www.aichatx.com.cn/blog/{filename}"

    new_article_html = template_content.replace("{{title}}", title)
    new_article_html = new_article_html.replace("{{description}}", description)
    new_article_html = new_article_html.replace("{{canonical_url}}", canonical_url)
    new_article_html = new_article_html.replace("{{date}}", today)
    new_article_html = new_article_html.replace("{{category}}", category)
    new_article_html = new_article_html.replace("{{read_time}}", str(read_time))
    new_article_html = new_article_html.replace("{{content}}", content)

    # 写入新的文章文件
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_article_html)
    print(f"成功生成文章: {filepath}")
    return {"title": title, "slug": f"{slug}.html", "description": description, "date": today, "category": category, "read_time": read_time}

def update_blog_index(new_articles_info):
    if not new_articles_info:
        return

    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        index_content = f.read()

    insert_point_match = re.search(r'(<div class="blog-grid">\s*)', index_content)
    if not insert_point_match:
        print("未找到博客列表插入点，请检查 blog/index.html 结构。")
        return

    insert_point_end = insert_point_match.end()
    
    # 准备新文章的 HTML 条目，按照逆序插入，确保最新文章在最前面
    new_entries_html = ""
    for article in reversed(new_articles_info): # 注意这里是 reversed
        entry_html = f"""
            <!-- Article: {article['title']} -->
            <a href="{article['slug']}" class="blog-card">
                <div class="blog-content">
                    <div class="blog-tag">{article['category']}</div>
                    <h2 class="blog-title">{article['title']}</h2>
                    <p class="blog-excerpt">{article['description']}</p>
                    <div class="blog-meta">
                        <span><i class="far fa-calendar"></i> {article['date']}</span>
                        <span><i class="far fa-clock"></i> {article['read_time']} 分钟阅读</span>
                    </div>
                </div>
            </a>
        """
        new_entries_html += entry_html

    # 插入新的文章条目到 index.html
    # 首先移除旧的 AI 生成文章，避免重复
    updated_index_content = re.sub(r'<!-- Article: .*? -->\s*<a href=".*?\.html" class="blog-card">.*?</a>', '', index_content, flags=re.DOTALL)
    # 然后在正确的位置插入新的
    updated_index_content = updated_index_content[:insert_point_end] + new_entries_html + updated_index_content[insert_point_end:]

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(updated_index_content)
    print(f"成功更新博客主页: {INDEX_FILE}")

def main(num_articles_to_generate=1):
    all_generated_blogs = load_generated_blogs() # 加载所有已生成的博客元数据
    generated_slugs = {blog['slug'] for blog in all_generated_blogs} # 存储已生成的slug

    random.shuffle(blog_posts_data) # 随机选择文章
    newly_generated_articles_info = []

    articles_generated_count = 0
    for post in blog_posts_data:
        slug_candidate = generate_slug(post["title"])
        if f"{slug_candidate}.html" in generated_slugs: # 检查是否已经生成过
            print(f"文章 '{post['title']}' (slug: {slug_candidate}.html) 已存在于 generated_blogs.json，跳过生成。")
            continue

        if articles_generated_count >= num_articles_to_generate:
            break

        article_info = create_blog_post(post)
        if article_info:
            newly_generated_articles_info.append(article_info)
            articles_generated_count += 1

    if newly_generated_articles_info:
        update_blog_index(newly_generated_articles_info)
        all_generated_blogs.extend(newly_generated_articles_info) # 将新生成的文章添加到总列表中
        save_generated_blogs(all_generated_blogs) # 保存更新后的列表

    if not newly_generated_articles_info:
        print("没有生成新的博客文章。可能所有文章都已生成或达到指定数量。")

if __name__ == "__main__":
    num_to_generate = 1
    if len(sys.argv) > 1:
        try:
            num_to_generate = int(sys.argv[1])
        except ValueError:
            print("请输入一个有效的数字作为生成文章的数量。")
            sys.exit(1)
    main(num_to_generate)
