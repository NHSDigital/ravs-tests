import {
  format,
  parse,
  addDays,
  subDays,
  differenceInCalendarYears,
  isValid,
  parseISO
} from 'date-fns';

export class BaseDatetimeHelper {
  static currentDatetime(): Date {
    return new Date();
  }

  static formatDatetime(dt: Date, fmt: string = 'yyyy-MM-dd HH:mm:ss'): string {
    return format(dt, fmt);
  }

  static parseDatetime(dateStr: string, fmt: string = 'yyyy-MM-dd HH:mm:ss'): Date {
    return parse(dateStr, fmt, new Date());
  }

  static addDays(dt: Date, days: number): Date {
    return addDays(dt, days);
  }

  static subtractDays(dt: Date, days: number): Date {
    return subDays(dt, days);
  }

  formatDate(date: string, browser: string): string {
    const formats = ['dd/MM/yyyy', 'yyyy-MM-dd', 'yyyy.MM.dd'];
    for (const fmt of formats) {
      const parsed = parse(date, fmt, new Date());
      if (isValid(parsed)) {
        return format(parsed, browser === 'safari' || browser === 'mobile' ? 'MM/dd/yyyy' : 'dd/MM/yyyy');
      }
    }
    throw new Error(
      'Invalid date format. Date should be in dd/mm/yyyy, yyyy-mm-dd, or yyyy.mm.dd.'
    );
  }

  getDateValueByDays(date: string): Date {
    const lower = date.trim().toLowerCase();

    if (lower.includes('today')) {
      const today = new Date();
      if (lower.includes('-')) {
        const offset = parseInt(lower.split('-')[1].trim(), 10);
        return subDays(today, offset);
      } else if (lower.includes('+')) {
        const offset = parseInt(lower.split('+')[1].trim(), 10);
        return addDays(today, offset);
      }
      return today;
    }

    return parseISO(lower);
  }

  getDateValueByMonths(date: string): Date {
    const lower = date.trim().toLowerCase();
    const today = new Date();

    if (lower.includes('today')) {
      if (lower.includes('-')) {
        const offset = parseInt(lower.split('-')[1].trim(), 10);
        if (offset >= 90) {
          return subDays(today, offset); // approx. 3 months
        } else if (offset >= 30) {
          return subDays(today, offset); // approx. 1 month
        } else if (offset >= 15) {
          return subDays(today, 15);
        } else {
          return subDays(today, offset);
        }
      } else if (lower.includes('+')) {
        const offset = parseInt(lower.split('+')[1].trim(), 10);
        return addDays(today, offset);
      }
      return today;
    }
    return parseISO(lower);
  }

  standardizeDateFormat(dateStr: string): string {
    const formats = ['dd/MM/yyyy', 'MM/dd/yyyy'];
    for (const fmt of formats) {
      const parsed = parse(dateStr, fmt, new Date());
      if (isValid(parsed)) {
        const day = parsed.getDate();
        const month = format(parsed, 'MM');
        const year = parsed.getFullYear();
        return `${day}/${month}/${year}`;
      }
    }
    return dateStr;
  }

  dateFormatWithAge(dateStr: string): string {
    const parsed = BaseDatetimeHelper.tryParseDate(dateStr) ?? null;
    if (!parsed) return dateStr;

    const today = new Date();
    const age = differenceInCalendarYears(today, parsed);
    const day = parsed.getDate();
    const month = format(parsed, 'MMMM');
    const year = parsed.getFullYear();

    return `${day} ${month} ${year} (aged ${age})`;
  }

  dateFormatWithDayOfWeek(dateStr: string): string {
    const parsed = BaseDatetimeHelper.tryParseDate(dateStr);
    if (!parsed) return dateStr;

    const day = parsed.getDate();
    const dayOfWeek = format(parsed, 'EEEE');
    const month = format(parsed, 'MMMM');
    const year = parsed.getFullYear();

    return `${dayOfWeek} ${day} ${month} ${year}`;
  }

  dateFormatWithNameOfMonth(dateStr: string): string {
    const parsed = BaseDatetimeHelper.tryParseDate(dateStr);
    if (!parsed) return dateStr;

    const day = parsed.getDate();
    const month = format(parsed, 'MMMM');
    const year = parsed.getFullYear();

    return `${day} ${month} ${year}`;
  }

  dateFormatWithNameOfMonthShortened(dateStr: string): string {
    const parsed = BaseDatetimeHelper.tryParseDate(dateStr);
    if (!parsed) return dateStr;

    const day = parsed.getDate();
    const month = format(parsed, 'MMM');
    const year = parsed.getFullYear();

    return `${day} ${month} ${year}`;
  }

  private static tryParseDate(dateStr: string): Date | null {
    const formats = ['dd/MM/yyyy', 'MM/dd/yyyy'];
    for (const fmt of formats) {
      const parsed = parse(dateStr, fmt, new Date());
      if (isValid(parsed)) return parsed;
    }
    return null;
  }
}

export class DatetimeHelper extends BaseDatetimeHelper {}
