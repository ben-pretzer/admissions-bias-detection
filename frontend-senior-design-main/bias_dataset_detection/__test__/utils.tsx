import { render } from '@testing-library/react'
import { rest } from 'msw'
import * as React from 'react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

export const handlers = [
    rest.get(
        '*/regions',
        (req, res, ctx) => {
            return res(
                ctx.status(200),
                ctx.json({
                    regions: ["Northwest"],
                })
            )
        }
    ),
    
    rest.get(
        '*/genders',
        (req, res, ctx) => {
            return res(
                ctx.status(200),
                ctx.json({
                    genders: ["Male"],
                })
            )
        }
    ),

    rest.get(
        '*/ethnicities',
        (req, res, ctx) => {
            return res(
                ctx.status(200),
                ctx.json({
                    ethnicities: ["Black"],
                })
            )
        }
    )
]

const createTestQueryClient = () => new QueryClient({
    defaultOptions: {
        queries: {
            retry: false,
        },
    },
    logger: {
        log: console.log,
        warn: console.warn,
        error: () => {},
    }
})

export function renderWithClient(ui: React.ReactElement) {
    const testQueryClient = createTestQueryClient()
    const { rerender, ...result } = render(
        <QueryClientProvider client={testQueryClient}>{ui}</QueryClientProvider>
    )
    return {
        ...result,
        rerender: (rerenderUi: React.ReactElement) =>
            rerender(
                <QueryClientProvider client={testQueryClient}>{rerenderUi}</QueryClientProvider>
            ),
    }
}

export function createWrapper() {
    const testQueryClient = createTestQueryClient()
    return ({ children }: {children: React.ReactNode}) => (
        <QueryClientProvider client={testQueryClient}>{children}</QueryClientProvider>
    )
}
