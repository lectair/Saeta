from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request):
    filters = [
        {
            "filter_title": "TOP COUNTRIES",
            "is_countries": True,
            "clickables": [
        {"clickable_name": "Korea, Republic of",
         "clickable_quantity": "64,938"
         },
        {"clickable_name": "United States",
         "clickable_quantity": "27,995"
         },
        {"clickable_name": "Taiwan",
         "clickable_quantity": "15,107"
         },
        {"clickable_name": "India",
         "clickable_quantity": "11,531"
         },
        {"clickable_name": "Japan",
         "clickable_quantity": "6,228"
         }
    ]
        },
        {
            "filter_title": "TOP ORGANIZATIONS",
            "is_countries": False,
            "clickables": [
            {"clickable_name": "Korea Telecom",
             "clickable_quantity": "4,751"
             },
            {"clickable_name": "Korean Education Network",
             "clickable_quantity": "3,026"
             },
            {"clickable_name": "Ministry of Wellbeing",
             "clickable_quantity": "1,614"
             },
            {"clickable_name": "SK Broadband Co Ltd",
             "clickable_quantity": "610"
             },
            {"clickable_name": "Hungary Comm",
             "clickable_quantity": "93"
             }
        ]
        },
        {
            "filter_title": "TOP PRODUCTS",
            "is_countries": False,
            "clickables": [
            {"clickable_name": "Canon printer control",
             "clickable_quantity": "724"
             },
            {"clickable_name": "Canon printer http",
             "clickable_quantity": "430"
             },
            {"clickable_name": "Apache httpd",
             "clickable_quantity": "176"
             },
            {"clickable_name": "BigIP",
             "clickable_quantity": "94"
             },
            {"clickable_name": "Dahua DVR",
             "clickable_quantity": "31"
             }
        ]
    }]
    results = [
        {
            "result_title": "리모트 UI: 로그인:MF633C/635C:MF633C/635C",
            "icon": "https://uploads-ssl.webflow.com/647dbb0b0e044a9ddaca5e0d/64804218675398ca9a745a8e_Button.png",
            "ip": "221.150.33.70",
            "org": "Korea Telecom",
            "country_name": "Republic of Korea, Gwangmyeong",
            "country_flag": "https://uploads-ssl.webflow.com/647dbb0b0e044a9ddaca5e0d/6480421a68750504aae2ad3b_image-2.png",
            "banner": "HTTP/1.1 200 OK\nDate: Mon, 05 Jun 2023 07:34:49 GMT\nServer: CANON HTTP Server\nContent-Type: text/html;charset=UTF-8\nSet-Cookie: view=normal;path=/\nSet-Cookie: language=ko;path=/\nSet-Cookie: kind=standard;path=/ pragma: no-cache\nCache-Control: no-store, no-cache, max-age=0\nExpires: Thu,01...",
            "timestamp": "2023-06-05T07:47:12.550414"
        },
        {
            "result_title": None,
            "icon": None,
            "ip": "121.153.113.20",
            "org": "SK Broadband Co Ltd",
            "country_name": "United States, Palo Alto",
            "country_flag": "https://uploads-ssl.webflow.com/647dbb0b0e044a9ddaca5e0d/6480421b76e4929467c1b68f_image-11.png",
            "banner": "SSH-2.0-OpenSSH_7.4\nKey type: ssh-rsa\nKey:AAAAB3NzaC1yc2EAAAADAQABAAABAQDI0aITPl2YJf4SzdB4fifwkQR/YHPerAkrRI0mKlQXRwY5\nE8hH9Z2xe9fMAoUu3qqqtNIpypHCeJQF2tXQkQJu1uWWWzaxbEwkHkDZMH1dbBkGDk37bRHMgr3U\nVmjn5fXzRWhrOl65yB5dAc5fBbF/ViAaEVTTxwwUL0Cv06qDr4k/1KUHh1JFZu+isDD88zD30FSa\n9yeuo+JhQQnmNTfZr/jIYdI...",
            "timestamp": "2023-06-05T07:32:56.709568"
        },
        {
            "result_title": "404 Not Found",
            "icon": "https://uploads-ssl.webflow.com/647dbb0b0e044a9ddaca5e0d/64804218675398ca9a745a8e_Button.png",
            "ip": "128.134.234.124",
            "org": "Korean Education Network",
            "country_name": "Republic of Korea, Seoul",
            "country_flag": "https://uploads-ssl.webflow.com/647dbb0b0e044a9ddaca5e0d/6480421a68750504aae2ad3b_image-2.png",
            "banner": "HTTP/1.1 404 Not Found\nServer: nginx/1.14.0 (Ubuntu)\nDate: Wed, 07 Jun 2023 11:11:51 GMT\nContent-Type: text/html\nContent-Length: 580\nConnection: keep-alive",
            "timestamp": "2023-06-05T07:32:52.661315"
        }
    ]
    total_results = f'{374012:,}'
    context = {'request': request, 'total_results': total_results, 'filters': filters, 'results': results}
    return templates.TemplateResponse("search.html", context)
