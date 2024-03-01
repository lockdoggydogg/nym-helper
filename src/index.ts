import express, { Request, Response, Application, NextFunction } from "express";
import cors from "cors";
import ApiError from "../utils/errors/ApiError";
import { InternalError } from "../utils/errors/CommonErrors";
import findByNodeName from "./parsingFunc";

const app: Application = express();
const port = process.env.PORT || 8000;

const start = async () => {
  try {
    app.listen(port, () => {
      console.log(`Server is Fire at http://localhost:${port}`);
    });
  } catch (e) {
    console.log(e);
  }
};

app.use(
  cors({
    origin: "http://localhost:3000",
    credentials: true,
  })
);
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.post("/routingScore", async (req: Request, res: Response) => {
  const reqBody = req.body;
  const nodeName = reqBody.name;

  console.log(await findByNodeName(nodeName))


  //   res.json({routingScore: 1}).status(200);
});

app.use((error: Error, req: Request, res: Response, next: NextFunction) => {
  if (error instanceof ApiError) {
    res.status(error.status).json({ err: error });
  } else {
    const internalError = new InternalError();
    res.status(500).json({ err: internalError });
  }
});

start();
