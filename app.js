import express from 'express';
import 'express-async-errors';
import cors from 'cors';
import morgan from 'morgan';
import helmet from 'helmet';
import cookieParser from 'cookie-parser';

import authRouter from './router/auth.js';
import receiptRouter from './router/receipt.js';
import partyRouter from './router/party.js';
import cartimageRouter from './router/cart.js';
import orderRouter from './router/order.js';
import paymentRouter from './router/payment.js';

import { config } from './config.js';
import {db} from './db/database.js';

const app = express(); 

const corsOption = {
    origin: config.cors.allowedOrigin,
    optionSuccessStatus: 200,
};

app.use(express.json());
app.use(cookieParser());
app.use(helmet());
app.use(cors(corsOption));
app.use(morgan('tiny'));

app.use('/auth', authRouter);
app.use('/profile', receiptRouter);
app.use('/category', partyRouter);
app.use('/presigned', cartRouter);
app.use('/speaking', orderRouter);
app.use('/test', paymentRouter);

app.use((req,res,next)=>{ 
    res.sendStatus(404);
});

app.use((error,req,res,next) => {
    console.error(error); 
    res.sendStatus(500); 
});

db.getConnection();

app.listen(config.port);
