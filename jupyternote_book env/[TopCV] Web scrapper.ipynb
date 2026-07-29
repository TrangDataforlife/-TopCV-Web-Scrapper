{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "09946a89-6107-44f1-90a2-c163bd23a396",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: bs4 in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (0.0.2)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from bs4) (4.13.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from beautifulsoup4->bs4) (2.6)\n",
      "Requirement already satisfied: typing-extensions>=4.0.0 in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from beautifulsoup4->bs4) (4.16.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: lxml in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (6.1.1)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: html5lib in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (1.1)\n",
      "Requirement already satisfied: six>=1.9 in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from html5lib) (1.17.0)\n",
      "Requirement already satisfied: webencodings in c:\\users\\admin\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from html5lib) (0.5.1)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.3 -> 26.1.2\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "! pip install bs4\n",
    "! pip install lxml\n",
    "! pip install html5lib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "dbaf4bf8-5772-4f1e-a1c9-1318faf2c8fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "3abe2361-6efa-41d0-a546-3d4e53476c72",
   "metadata": {},
   "outputs": [],
   "source": [
    "base_url = 'https://www.topcv.vn/tim-viec-lam-data-analyst-tai-ho-chi-minh-kl2?type_keyword=1&sba=1&locations=l2'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "8c24bfc2-b76f-497c-951a-5d1499e7af82",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Headers for request\n",
    "HEADERS = ({\n",
    "                'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36', \n",
    "                'Accepted-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8' })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "60b686fe-b4a9-4ce5-927a-4bdaf4755d8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "page = requests.get(base_url, headers = HEADERS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "c711378a-5b46-4a4a-b1f7-f411d7bfacc8",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(page.content, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "7cfa6b9c-3aab-4a77-b9db-71b66130c905",
   "metadata": {},
   "outputs": [],
   "source": [
    "job_links = soup.find_all('a', attrs={'aria-label': True})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "90176847-ceb7-4dcb-a142-54b39af587f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[\n",
      "    {\n",
      "        \"job_title\": \"Data Analyst Ngân Hàng Shinhan\",\n",
      "        \"company_name\": \"Ngân Hàng TNHH MTV Shinhan Việt Nam\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/data-analyst-ngan-hang-shinhan/2174212.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"31/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Data Analyst Workforce Management_App Social Video\",\n",
      "        \"company_name\": \"CÔNG TY TNHH TRANSCOSMOS VIỆT NAM\",\n",
      "        \"link\": \"https://www.topcv.vn/brand/transcosmoshochiminh/tuyen-dung/data-analyst-workforce-management-app-social-video-j2238139.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"31/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Dữ Liệu / Data Executive / Bắt Buộc Biết Tiếng Trung / Quận 7\",\n",
      "        \"company_name\": \"CÔNG TY TNHH NEXTAD STUDIO\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-du-lieu-data-executive-bat-buoc-biet-tieng-trung-quan-7/2046581.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"31/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"CVM Manager (Ưu Tiên Có Kn Strategy & Analytics)\",\n",
      "        \"company_name\": \"Công Ty Tài Chính Tổng hợp Cổ Phần Tín Việt\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/cvm-manager-uu-tien-co-kn-strategy-analytics/2245117.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh,Hà Nội\",\n",
      "        \"experience\": \"Trên 5 năm\",\n",
      "        \"deadline\": \"20/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Data Analytics Lead\",\n",
      "        \"company_name\": \"CÔNG TY TNHH DỊCH VỤ SECOM\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/data-analytics-lead/2232005.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"5 năm\",\n",
      "        \"deadline\": \"09/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Risk Management Specialist (CV Quản Lý Rủi Ro)\",\n",
      "        \"company_name\": \"Công Ty Tài Chính Tổng hợp Cổ Phần Tín Việt\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/risk-management-specialist-cv-quan-ly-rui-ro/2220752.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"30/07/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Phân Tích Dữ Liệu Vận Hành\",\n",
      "        \"company_name\": \"CÔNG TY CỔ PHẦN CARPLA\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-phan-tich-du-lieu-van-hanh/2245988.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"22/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Data Analyst (Leader)\",\n",
      "        \"company_name\": \"CÔNG TY CỔ PHẦN CÔNG NGHỆ ALPHAWAY\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/data-analyst-leader/2245403.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"3 năm\",\n",
      "        \"deadline\": \"21/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Risk Analysis\",\n",
      "        \"company_name\": \"Công Ty Tài Chính Tổng hợp Cổ Phần Tín Việt\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/risk-analysis/2227463.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"05/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Phân Tích Vận Hành Và Quản Trị Dữ Liệu (DGA/ Analytics Engineer)\",\n",
      "        \"company_name\": \"CELLPHONES\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-phan-tich-van-hanh-va-quan-tri-du-lieu-dga-analytics-engineer/2226731.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"2 năm\",\n",
      "        \"deadline\": \"05/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Phân Tích Thống Kê\",\n",
      "        \"company_name\": \"Công ty TNHH Thực Phẩm Thái Sơn\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-phan-tich-thong-ke/325305.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"2 năm\",\n",
      "        \"deadline\": \"18/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Phân Tích Dữ Liệu (Kênh Trả Góp)\",\n",
      "        \"company_name\": \"CÔNG TY TÀI CHÍNH TRÁCH NHIỆM HỮU HẠN MỘT THÀNH VIÊN LOTTE VIỆT NAM\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-phan-tich-du-lieu-kenh-tra-gop/2223692.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"02/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Data Management Executive\",\n",
      "        \"company_name\": \"Công ty Cổ phần METUB Việt Nam\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/data-management-executive/2223403.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"2 năm\",\n",
      "        \"deadline\": \"01/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Data Analyst (Workforce Management)\",\n",
      "        \"company_name\": \"Công ty TNHH Vietnam Concentrix Services\",\n",
      "        \"link\": \"https://www.topcv.vn/brand/concentrixservices/tuyen-dung/data-analyst-workforce-management-j2236885.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"14/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Data Analyst (Middle Level)\",\n",
      "        \"company_name\": \"CÔNG TY TNHH AMARIS VIỆT NAM\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/data-analyst-middle-level/2219379.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"2 năm\",\n",
      "        \"deadline\": \"29/07/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Lead Phân Tích Dữ Liệu (Data Analyst)\",\n",
      "        \"company_name\": \"CÔNG TY CỔ PHẦN CÔNG NGHỆ SICIX\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/lead-phan-tich-du-lieu-data-analyst/2230421.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hà Nội,Hồ Chí Minh\",\n",
      "        \"experience\": \"3 năm\",\n",
      "        \"deadline\": \"08/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Quản Trị Và Vận Hành Misa Amis - Không Kinh Nghiệm\",\n",
      "        \"company_name\": \"CÔNG TY TNHH MTV KỸ THUẬT TÚ LỘC\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/quan-tri-va-van-hanh-misa-amis-khong-kinh-nghiem/2228691.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"Không yêu cầu\",\n",
      "        \"deadline\": \"06/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Khai Thác Số Liệu\",\n",
      "        \"company_name\": \"Ngân Hàng Thương Mại Cổ Phần Kiên Long\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-khai-thac-so-lieu/2225914.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"3 năm\",\n",
      "        \"deadline\": \"05/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Chuyên Viên Phân Tích Yêu Cầu\",\n",
      "        \"company_name\": \"CÔNG TY TNHH VTTECH\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/chuyen-vien-phan-tich-yeu-cau/2224166.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"1 năm\",\n",
      "        \"deadline\": \"02/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"Thực Tập Sinh Phân Tích Đầu Tư\",\n",
      "        \"company_name\": \"CÔNG TY TNHH ĐẦU TƯ VÀ PHÁT TRIỂN FINTOP\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/thuc-tap-sinh-phan-tich-dau-tu/1865273.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hà Nội,Hồ Chí Minh\",\n",
      "        \"experience\": \"Không yêu cầu\",\n",
      "        \"deadline\": \"01/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"HR Data Analyst Supervisor\",\n",
      "        \"company_name\": \"Công Ty Cổ Phần Dược Phẩm Pharmacity\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/hr-data-analyst-supervisor/2223597.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"3 năm\",\n",
      "        \"deadline\": \"01/08/2026\"\n",
      "    },\n",
      "    {\n",
      "        \"job_title\": \"BI Data\",\n",
      "        \"company_name\": \"CÔNG TY CỔ PHẦN DỊCH  VỤ CÔNG NGHỆ TIN HỌC HPT\",\n",
      "        \"link\": \"https://www.topcv.vn/viec-lam/bi-data/2040175.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203\",\n",
      "        \"location\": \"Hồ Chí Minh\",\n",
      "        \"experience\": \"2 năm\",\n",
      "        \"deadline\": \"31/07/2026\"\n",
      "    }\n",
      "]\n"
     ]
    }
   ],
   "source": [
    "link_list = []\n",
    "for job in job_links:\n",
    "    href = job.get('href')\n",
    "    # Chỉ lấy link thật, bỏ qua javascript popup và None\n",
    "    if href and href.startswith('https://www.topcv.vn/'):\n",
    "        link_list.append(href)\n",
    "\n",
    "data = []\n",
    "for link in link_list:\n",
    "    # Retry khi gặp lỗi 429 (Rate Limit)\n",
    "    while True:\n",
    "        new_webpage = requests.get(link, headers=HEADERS)\n",
    "        if new_webpage.status_code == 429:\n",
    "            print(\"Bị chặn 429, đợi lâu hơn rồi thử lại...\")\n",
    "            time.sleep(random.uniform(15, 30))\n",
    "            continue\n",
    "        break\n",
    "\n",
    "    new_soup = BeautifulSoup(new_webpage.content, 'lxml')\n",
    "\n",
    "    # Trích xuất Tên công việc\n",
    "    job_title_element = new_soup.find('h1', class_='box-header-job__title')\n",
    "    job_title = \" \".join(job_title_element.text.split()) if job_title_element else ''\n",
    "\n",
    "    # Trích xuất Tên công ty\n",
    "    company_name_el = new_soup.find('a', class_='name')\n",
    "    company_name = company_name_el.text.strip() if company_name_el else ''\n",
    "\n",
    "    # Khởi tạo Dictionary theo đúng thứ tự bạn yêu cầu\n",
    "    job_info = {\n",
    "        'job_title': job_title,      # 1. Tên công việc\n",
    "        'company_name': company_name, # 2. Tên công ty\n",
    "        'link': link,                 # 3. Đường link\n",
    "        'location': '',               # 4. Địa điểm\n",
    "        'experience': '',             # 5. Kinh nghiệm\n",
    "        'deadline': ''                # 6. Hạn ứng tuyển\n",
    "    }\n",
    "\n",
    "    # Bổ sung các thông tin chi tiết\n",
    "    for item in new_soup.find_all('div', class_='list-info__content'):\n",
    "        title_el = item.find('div', class_='list-info__content__title')\n",
    "        desc_el = item.find('div', class_='list-info__content__desc')\n",
    "\n",
    "        title = title_el.get_text(strip=True) if title_el else ''\n",
    "        desc = desc_el.get_text(strip=True) if desc_el else ''\n",
    "\n",
    "        if 'Địa điểm' in title:\n",
    "            job_info['location'] = desc\n",
    "        elif 'Kinh nghiệm' in title:\n",
    "            job_info['experience'] = desc\n",
    "        elif 'Hạn' in title:\n",
    "            job_info['deadline'] = desc\n",
    "\n",
    "    data.append(job_info)\n",
    "    \n",
    "    # Nghỉ 1 lần ngắn sau mỗi link thay vì nghỉ nhiều lần rải rác\n",
    "    time.sleep(random.uniform(3, 7))\n",
    "\n",
    "# In dữ liệu dạng dễ nhìn (Pretty Print)\n",
    "import json\n",
    "print(json.dumps(data, ensure_ascii=False, indent=4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "e82b73b2-de8b-409d-b5db-8b820e8a0cd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Đã lưu dữ liệu vào jobs.json\n"
     ]
    }
   ],
   "source": [
    "# Lưu kết quả ra file JSON\n",
    "with open(\"jobs.json\", \"w\", encoding=\"utf-8\") as f:\n",
    "    json.dump(data, f, ensure_ascii=False, indent=4)\n",
    "print(\"Đã lưu dữ liệu vào jobs.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "8ff2cafc-c232-4c1f-9f21-20d2c8547af5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Đã xuất file thành công!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Giả sử bạn đã thu thập xong list data ở trên\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Đổi lại tên cột hiển thị bằng tiếng Việt nếu muốn (Tùy chọn)\n",
    "df = df.rename(columns={\n",
    "    'job_title': 'Tên công việc',\n",
    "    'company_name': 'Tên công ty',\n",
    "    'link': 'Đường link',\n",
    "    'location': 'Địa điểm',\n",
    "    'experience': 'Kinh nghiệm',\n",
    "    'deadline': 'Hạn ứng tuyển'\n",
    "})\n",
    "\n",
    "# Xuất ra file CSV (dùng utf-8-sig để xem tiếng Việt chuẩn trong Excel)\n",
    "df.to_csv('topcv_jobs_pandas.csv', index=False, encoding='utf-8-sig')\n",
    "\n",
    "print(\"Đã xuất file thành công!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f705cae9-686e-4104-bb9a-57a2ebc7bf24",
   "metadata": {},
   "source": [
    "2/ Lấy đại diện để test code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "14d64d6f-3d50-4f87-bb05-b1fd27abf489",
   "metadata": {},
   "outputs": [],
   "source": [
    "job_list = link_list[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "2d8b8e04-9cc3-4b09-a4e6-fe9cbff9b4ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.topcv.vn/viec-lam/data-analyst-ngan-hang-shinhan/2174212.html?ta_source=JobSearchList_LinkDetail&u_sr_id=PkRogDac2NRCf3nmn5mk1q3ApbNYunwCQqlnDdeg_1785251203'"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "job_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "a3777f61-cd0c-4acc-aa06-3006ab5c4846",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_webpage = requests.get(job_list, headers = HEADERS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "610ebdb5-39ce-40e6-8db5-b9a461eb46bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_webpage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "aa30e6d5-adfe-45fe-a3bc-ac48d06a1636",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_soup = BeautifulSoup(new_webpage.content, 'lxml')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "2907cf85-106c-44f0-9e3c-2d4bf82aac52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data Analyst Ngân Hàng Shinhan\n"
     ]
    }
   ],
   "source": [
    "# Tìm thẻ h1 chứa tên công việc\n",
    "job_title_element = new_soup.find('h1', class_='box-header-job__title')\n",
    "\n",
    "# Lấy toàn bộ text, dùng strip=True để loại bỏ khoảng trắng thừa ở đầu/cuối\n",
    "job_title = \" \".join(job_title_element.text.split())\n",
    "print(job_title)\n",
    "# Kết quả: \"Data Analyst Ngân Hàng Shinhan\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "afbc3b7e-b20c-4a25-86cd-47757434f6d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ngân Hàng TNHH MTV Shinhan Việt Nam\n"
     ]
    }
   ],
   "source": [
    "company_name = new_soup.find('a', class_='name')\n",
    "company_name = company_name.text\n",
    "print(company_name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "97cad3fc-76fb-45ee-8514-4021d8198fa1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Địa điểm: Hồ Chí Minh\n",
      "Kinh nghiệm: 1 năm\n",
      "Hạn ứng tuyển: 31/08/2026\n"
     ]
    }
   ],
   "source": [
    "data = []\n",
    "\n",
    "# Duyệt qua từng khung chứa thông tin\n",
    "for item in new_soup.find_all('div', class_='list-info__content'):\n",
    "    # Lấy element title và desc bên trong khung đó\n",
    "    title_el = item.find('div', class_='list-info__content__title')\n",
    "    desc_el = item.find('div', class_='list-info__content__desc')\n",
    "    \n",
    "    # Lấy văn bản và xóa khoảng trắng thừa (strip=True)\n",
    "    title = title_el.get_text(strip=True) if title_el else ''\n",
    "    desc = desc_el.get_text(strip=True) if desc_el else ''\n",
    "    \n",
    "    data.append({\n",
    "        'title': title,\n",
    "        'description': desc\n",
    "    })\n",
    "\n",
    "# In kết quả kiểm tra\n",
    "for d in data:\n",
    "    print(f\"{d['title']}: {d['description']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1cc81d28-872b-4c0c-909f-e1b068120292",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
