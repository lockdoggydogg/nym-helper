import * as cheerio from "cheerio";
import { MAIN_URL } from "./consts";
import puppeteer from "puppeteer";

const findByNodeName = async (nodeName: string) => {
  try {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.setViewport({ width: 1730, height: 10560 });
    await page.goto(MAIN_URL, { waitUntil: "networkidle0" });

    const pageSourceHTML = await page.content();

    const $ = cheerio.load(pageSourceHTML);

    let rs = $(".chakra-text.css-9jsfde").filter(function () {
              return $(this).text().trim() === nodeName;
            })
            .text();

    // const scrolling = () => {
    //   const scrollable_section = ".table";

    //   console.log(
    //     $(scrollable_section).
    //         .filter(function () {
    //           return $(this).text().trim() === nodeName;
    //         })
    //         .text()
    //   );

    // scrolling();

    //   if (
    //       .filter(function () {
    //         return $(this).text().trim() === nodeName;
    //       })
    //       .text() == nodeName) {
        rs = $(".chakra-text.css-9jsfde")
          .filter(function () {
            return $(this).text().trim() === nodeName;
          })
          .parent()
          .parent()
          .parent()
          .next()
          .next()
          .next()
          .next()
          .next()
          .next()
          .text();
    //   } else {
    //     await page.focus(scrollable_section);
    //     await page.keyboard.press("Space");
    //     scrolling();
    //   }
    // };

    // scrolling();

    browser.close();

    return rs;
  } catch (err) {
    console.error(err);
  }
};

export default findByNodeName;
