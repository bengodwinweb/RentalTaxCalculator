import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth

from taxcalculator.yearlytax import YearlyTax
from taxcalculator.quarterlytax import QuarterlyTax

PAGE_WIDTH = letter[0]
PAGE_HEIGHT = letter[1]

TITLE_FONT = 'Helvetica-Bold'
TITLE_SIZE = 24
TITLE_Y = 10 * inch

HEADING_FONT = 'Helvetica-Bold'
HEADING_SIZE = 16

FONT = 'Helvetica'
FONT_SIZE = 12
ROW_HEIGHT = 13

KEY_FORMAT = '{:<50s}'
AMOUNT_FORMAT = '${:>12,.2f}'
COLUMN_GAP = .25 * inch

SIGN_X = 3.3 * inch
OFFSET_X = inch


def draw_num_row(c: Canvas, y: int, right_x: int, key: str, val: int):
    c.drawString(inch, y, key)
    c.drawRightString(right_x, y, str(val))


def draw_finance_row(c: Canvas, y: int, sign_x: int, right_offset: int, key: str, val: float):
    c.drawString(inch, y, key)
    c.drawString(sign_x, y, '$')
    c.drawRightString(sign_x + right_offset, y, '{:,.2f}'.format(val))


def draw_quarter(c: Canvas, x: int, y: int, quarterly_tax: QuarterlyTax) -> tuple:
    y -= .5 * inch
    x = inch
    c.setFont(HEADING_FONT, HEADING_SIZE)
    c.drawString(x, y, 'Quarter ' + str(quarterly_tax.quarterNum))

    c.setFont(FONT, FONT_SIZE)
    x = 4.5 * inch
    y -= 20
    draw_finance_row(c, y, SIGN_X, OFFSET_X, 'Gross Income', quarterly_tax.gross)
    y -= ROW_HEIGHT
    draw_finance_row(c, y, SIGN_X, OFFSET_X, 'Taxable Income', quarterly_tax.taxableIncome)
    # c.drawRightString(x - COLUMN_GAP, y, KEY_FORMAT.format('Taxable Income'))
    y -= ROW_HEIGHT
    draw_finance_row(c, y, SIGN_X, OFFSET_X, 'Sales Tax Collected', quarterly_tax.salesTaxCollected)
    y -= ROW_HEIGHT
    draw_finance_row(c, y, SIGN_X, OFFSET_X, 'Sales Tax Owed', quarterly_tax.salesTaxOwed)
    y -= ROW_HEIGHT
    draw_finance_row(c, y, SIGN_X, OFFSET_X, 'Occupancy Tax Collected', quarterly_tax.occupancyTaxCollected)
    y -= ROW_HEIGHT
    draw_finance_row(c, y, SIGN_X, OFFSET_X, 'Occupancy Tax Owed', quarterly_tax.occupancyTaxOwed)
    y -= ROW_HEIGHT
    draw_num_row(c, y, SIGN_X + OFFSET_X, 'Nights Booked', quarterly_tax.nightsBooked)

    return x, y


def make_pdf(fname: str, yearly_tax: YearlyTax):
    """
    Creates a PDF summary of the YearlyTax and places it at fname
    @param fname: path to output file
    @type fname: str
    @param yearly_tax: calculated tax
    @type yearly_tax: YearlyTax
    """
    if os.path.exists(fname):
        os.remove(fname)

    canvas = Canvas(fname, letter)

    # title
    title_text = 'Income Tax - ' + str(yearly_tax.year)
    title_width = stringWidth(title_text, TITLE_FONT, TITLE_SIZE)
    canvas.setFont(TITLE_FONT, TITLE_SIZE)
    canvas.drawString((PAGE_WIDTH - title_width) / 2.0, TITLE_Y, title_text)

    # yearly fields
    x = 3 * inch
    y = TITLE_Y - (.75 * inch)
    canvas.setFont(FONT, 14)
    draw_finance_row(canvas, y, SIGN_X - 10, OFFSET_X + 10, 'Gross Income', yearly_tax.gross)
    y -= 20
    draw_finance_row(canvas, y, SIGN_X - 10, OFFSET_X + 10, 'Taxable Income', yearly_tax.taxableIncome)
    y -= 20
    draw_num_row(canvas, y, SIGN_X + OFFSET_X, 'Nights Booked', yearly_tax.nightsBooked)

    coords = draw_quarter(canvas, x, y, yearly_tax.quarter1)
    x = coords[0]
    y = coords[1]
    coords = draw_quarter(canvas, x, y, yearly_tax.quarter2)
    x = coords[0]
    y = coords[1]
    coords = draw_quarter(canvas, x, y, yearly_tax.quarter3)
    x = coords[0]
    y = coords[1]
    coords = draw_quarter(canvas, x, y, yearly_tax.quarter4)

    canvas.save()
