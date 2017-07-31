'use strict';

import { REQUEST_TIMEOUT } from '../lib/constants';
import { default as baseRequest } from 'request';
const request = baseRequest.defaults({timeout: REQUEST_TIMEOUT});
import cheerio from 'cheerio';
import { flattenDeep } from 'lodash';
import { parallel } from 'async';
import { default as moment } from 'moment-timezone';


export const name = '{{ cookiecutter.adapter_name }}';

export function fetchData (source, cb) {
  return cb(null, []);
}
